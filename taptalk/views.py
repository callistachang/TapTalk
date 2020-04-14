from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib import messages

from articles.models import Article
from users.models import User, Expert, CommonUser
from comments.models import Comment
from sections.models import Section
import config

import facebook
import requests


class MainView(generic.ListView):
    template_name = 'main.html'
    context_object_name = 'article_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['linkedin_login'] = config.LINKEDIN_LOGIN_URL
        context['facebook_login'] = config.FACEBOOK_LOGIN_URL
        return context

    def get_queryset(self):
        return Article.objects.all()

# TODO: LinkedIn and FB integration


class ProfileView(generic.DetailView):
    model = User
    template_name = 'profile.html'

# TODO: Fetch comments as well
# TODO: Change to class-based view?
# def article(request, article_id):
#     article = get_object_or_404(Article, pk=article_id)
#     context ={
#         'article': article,
#     }
#     return render(request, 'article.html', context)


class ArticleView(generic.DetailView):
    model = Article
    template_name = 'article.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['linkedin_login'] = config.LINKEDIN_LOGIN_URL
        context['facebook_login'] = config.FACEBOOK_LOGIN_URL
        context['linkedin_logo'] = config.LINKEDIN_LOGIN_LOGO
        context['facebook_logo'] = config.FACEBOOK_LOGIN_LOGO
        context['expert_comments'] = Comment.objects.get_expert_comments()
        context['user_comments'] = Comment.objects.get_user_comments()

        self.request.session['article_id'] = self.kwargs['pk']

        return context

# TODO: Section is hardcoded to 1


def post_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = request.POST['Comment']
    user = User.objects.get(pk=request.session['user_id'])
    # user = User.objects.get(pk='1')
    section = Section.objects.get(id=1)
    print(article, content, user)

    context = {
        'article': article,
    }

    if not Comment.objects.create_comment(content, section, user, article):
        messages.error(request, 'You are not allowed to post that comment.')
    else:
        messages.success(request, 'The comment was posted successfully!')

    # messages.success(request, _('Thank you'))

    return HttpResponseRedirect('/article/' + str(article.id))

# Expert verification


def upvote(request, article_id, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    messages.info(request, 'The comment was upvoted successfully!')

    # article = Article.sections.

    # article = comment.article_section.article_set.all()
    comment.num_votes += 1
    comment.save()
    return HttpResponseRedirect('/article/' + '1')


def linkedin_auth(request):
    token_params = {
        'grant_type': 'authorization_code',
        'redirect_uri': config.LINKEDIN_REDIRECT_URL,
        'client_id': config.LINKEDIN_CLIENT_ID,
        'client_secret': config.LINKEDIN_CLIENT_SECRET,
        'code': request.GET['code']
    }

    # Get access token
    token_request = requests.get(
        config.LINKEDIN_TOKEN_URL, params=token_params)
    token = token_request.json()['access_token']

    info_headers = {
        'Authorization': 'Bearer ' + token
    }
    email_params = {
        'q': 'members',
        'projection': '(elements*(primary,type,handle~))'
    }

    r = requests.get(
        "https://api.linkedin.com/v2/recommendedJobs?q=byMember", headers=info_headers)
    print(r.json())

    # # Get email
    # email_request = requests.get(config.LINKEDIN_GET_EMAIL_URL, headers=info_headers, params=email_params)
    # email = email_request.json()['elements'][0]['handle~']['emailAddress']

    # # Find out if they already exist in the database.
    # # If they are, retrieve the data.
    # # If they aren't, add them to the database.
    # try:
    #     expert = Expert.objects.get(email=email)
    # except:
    #     # Get name
    #     name_request = requests.get(config.LINKEDIN_GET_NAME_URL, headers=info_headers)
    #     name = name_request.json()['localizedFirstName'] + ' ' + name_request.json()['localizedLastName']
    #     # Create new expert
    #     expert = Expert.objects.create(email=email, name=name, expert_title="Hardcoded Expert Title")

    # request.session['user_name'] = expert.name
    # request.session['user_id'] = expert.id

    return HttpResponseRedirect('/article/' + str(request.session['article_id']))

# Facebook verification


def facebook_auth(request):
    token_params = {
        'client_id': config.FACEBOOK_APP_ID,
        'redirect_uri': config.FACEBOOK_REDIRECT_URL,
        'client_secret': config.FACEBOOK_APP_SECRET,
        'code': request.GET['code']
    }

    # Get access token
    token_request = requests.get(
        config.FACEBOOK_TOKEN_URL, params=token_params)
    token = token_request.json()['access_token']

    graph = facebook.GraphAPI(access_token=token, version="2.12")
    info = graph.get_object("me")

    try:
        user = CommonUser.objects.get(facebook_id=info['id'])
    except:
        user = CommonUser.objects.create(
            name=info['name'], facebook_id=info['id'])

    request.session['user_name'] = user.name
    request.session['user_id'] = user.id

    return HttpResponseRedirect('/article/' + str(request.session['article_id']))
