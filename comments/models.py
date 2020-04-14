from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User, CommonUser, Expert
from sections.models import Section
import config

import requests

# Returns True if it is <0.8 toxic according to Perspective API


def is_comment_valid(content):
    headers = {
        "Content-Type": "application/json"
    }
    data = '{comment: {text: "' + content + \
        '"}, languages: ["en"], requestedAttributes: {TOXICITY:{}}}'
    payload = {
        "key": config.PERSPECTIVE_API_KEY
    }

    r = requests.post(config.PERSPECTIVE_API_URL,
                      headers=headers, data=data, params=payload)

    toxicity_score = r.json(
    )['attributeScores']['TOXICITY']['spanScores'][0]['score']['value']
    print(toxicity_score)

    if toxicity_score > 0.8:
        return False
    else:
        return True


class CommentManager(models.Manager):
    def create_comment(self, content, section, creator, parent_comment=None):
        # Comment passes the Perspective API check
        if is_comment_valid(content):
            comment_type = 'E'
            if isinstance(creator, CommonUser):
                comment_type = 'U'
            Comment.objects.create(content=content, article_section=section,
                                   comment_type=comment_type, creator=creator, parent_comment=None)
            return True
        else:
            return False

    def get_expert_comments(self):
        return self.filter(comment_type='E').order_by('-num_votes')

    def get_user_comments(self):
        return self.filter(comment_type='U').order_by('-num_votes')


class Comment(models.Model):
    """Model definition for Comment."""

    class CommentType(models.TextChoices):
        EXPERT = 'E', _('Expert')
        COMMON_USER = 'U', _('User')

    id = models.AutoField(primary_key=True)
    num_votes = models.IntegerField(default=0, blank=True)
    num_shares = models.IntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    parent_comment = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    # Necessary fields
    content = models.TextField()
    comment_type = models.CharField(
        choices=CommentType.choices, max_length=1, default='U')
    article_section = models.ForeignKey(
        Section, related_name='comments', on_delete=models.CASCADE)
    creator = models.ForeignKey(
        User, related_name='comments', on_delete=models.CASCADE)

    objects = CommentManager()

    class Meta:
        """Meta definition for Comment."""

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content
