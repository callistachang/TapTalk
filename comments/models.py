from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from articles.models import Article

import requests

# Returns True if it is <0.8 toxic according to Perspective API
def is_comment_valid(content):
    API_KEY = "AIzaSyASESEjSGvyXs-3ySiJeJ99fOFn7RL118I"
    API_URL = "https://commentanalyzer.googleapis.com/v1alpha1/comments:analyze"

    headers = {
        "Content-Type": "application/json"
    }
    data = '{comment: {text: "' + content + '"}, languages: ["en"], requestedAttributes: {TOXICITY:{}}}'
    payload = {
        "key": API_KEY
    }

    r = requests.post(API_URL, headers=headers, data=data, params=payload)

    toxicity_score = r.json()['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']
    print(toxicity_score)
    
    if toxicity_score > 0.8:
        return False
    else:
        return True

class CommentManager(models.Manager):
    def create_comment(self, content, creator, article, section):
        if is_comment_valid(content):
            Comment.objects.create(content=content, section=1, creator=creator, article=article)
            return True
        else:
            return False
        # if not is_comment_valid():
        #     return None
        # else:
        #     comment = self.create()
        # return comment

class Comment(models.Model):
    """Model definition for Comment."""

    class CommentType(models.TextChoices):
        EXPERT = 'E', _('Expert')
        COMMON_USER = 'U', _('User')

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    num_votes = models.IntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    section = models.IntegerField()
    comment_type = models.CharField(choices=CommentType.choices, max_length=1, blank=True, default='U')  # Automatically set
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='children_comments', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    objects = CommentManager()

    class Meta:
        """Meta definition for Comment."""  

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content
        # return "Comment by " + str(self.creator) + " on \"" + str(self.article) + "\""