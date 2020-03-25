from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

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
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context ={
        'article': article,
    }
    return render(request, 'article.html', context)

# TODO: User is hardcoded to be Obama, section is hardcoded to 1
def post_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = request.POST['Comment']
    user = User.objects.get(pk=2)
    section = Section.objects.get(id=1)
    print(article, content, user)

    context = {
        'article': article,
    }

    if not Comment.objects.create_comment(content, section, user, article):
        context['msg'] = 'You are not allowed to post that comment as it is toxic.'
    else:
        context['msg'] = 'The comment was posted successfully.'

    return render(request, 'article.html', context)

# Expert verification
def linkedin_auth(request):
    token_params = {
        'grant_type': 'authorization_code',
        'redirect_uri': config.LINKEDIN_REDIRECT_URL,
        'client_id': config.LINKEDIN_CLIENT_ID,
        'client_secret': config.LINKEDIN_CLIENT_SECRET,
        'code': request.GET['code']
    }

    # Get access token
    token_request = requests.get(config.LINKEDIN_TOKEN_URL, params=token_params)
    token = token_request.json()['access_token']

    info_headers = {
        'Authorization': 'Bearer ' + token
    }
    email_params = {
        'q': 'members',
        'projection': '(elements*(primary,type,handle~))'
    }

    # Get email
    email_request = requests.get(config.LINKEDIN_GET_EMAIL_URL, headers=info_headers, params=email_params)
    email = email_request.json()['elements'][0]['handle~']['emailAddress']

    # Find out if they already exist in the database.
    # If they are, retrieve the data.
    # If they aren't, add them to the database.
    try:
        expert = Expert.objects.get(email=email)
    except:
        # Get name
        name_request = requests.get(config.LINKEDIN_GET_NAME_URL, headers=info_headers)
        name = name_request.json()['localizedFirstName'] + ' ' + name_request.json()['localizedLastName']
        # Create new expert
        expert = Expert.objects.create(email=email, name=name, expert_title="Hardcoded Expert Title")

    print(expert)

    return HttpResponseRedirect(reverse('main'))
    # return render(request, 'main.html')

# Facebook verification
def facebook_auth(request):
    token_params = {
        'client_id': config.FACEBOOK_APP_ID,
        'redirect_uri': config.FACEBOOK_REDIRECT_URL,
        'client_secret': config.FACEBOOK_APP_SECRET,
        'grant_type': 'client_credentials',
        'code': request.GET['code']
    }

    # Get access token
    token_request = requests.get(config.LINKEDIN_TOKEN_URL, params=token_params)

    print(token_request.content)

    token = token_request.json()['access_token']

    graph = facebook.GraphAPI(access_token=token, version="2.12")
    info = graph.get_object("me")

    try:
        user = CommonUser.objects.get(facebook_id=info['id'])
    except:
        # Create new user
        user = CommonUser.objects.create(name=info['name'], facebook_id=info['id'])

    print(user)

    return HttpResponseRedirect(reverse('main'))