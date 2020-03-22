from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from articles.models import Article
from users.models import User, Expert
from comments.models import Comment

class MainView(generic.ListView):
    template_name = 'main.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        return Article.objects.all()

# TODO: Fetch comments as well
# TODO: Change to class-based view?
def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    context ={
        'article': article,
        'error_msg': None
    }
    return render(request, 'article.html', context)

# TODO: LinkedIn and FB integration
class ProfileView(generic.DetailView):
    model = User
    template_name = 'profile.html'

# TODO: User is hardcoded to be Obama, section is hardcoded to 1
def post_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    content = request.POST['Comment']
    user = User.objects.get(pk=2)

    context = {
        'article': article,
    }

    if not Comment.objects.create_comment(content, 1, user, article):
        context['msg'] = 'You are not allowed to post that comment as it is toxic.'
    else:
        context['msg'] = 'The comment was posted successfully.'

    return render(request, 'article.html', context)
