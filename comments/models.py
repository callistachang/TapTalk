from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User
from articles.models import Article

COMMENT_TYPES = (

)

class Comment(models.Model):
    """Model definition for Comment."""

    class CommentType(models.TextChoices):
        EXPERT = 'E', _('Expert')
        COMMON_USER = 'U', _('User')

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    num_votes = models.IntegerField()
    date_posted = models.DateTimeField(auto_now_add=True)
    section = models.IntegerField()
    comment_type = models.CharField(choices=CommentType.choices, max_length=1)
    parent_comment_id = models.ForeignKey('self', null=True, related_name='children_comments', on_delete=models.CASCADE)
    creator_id = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comment."""  

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        """Unicode representation of Comment."""
        pass