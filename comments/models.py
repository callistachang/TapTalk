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
    num_votes = models.IntegerField(default=0, blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    section = models.IntegerField()
    comment_type = models.CharField(choices=CommentType.choices, max_length=1)  # Automatically set
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='children_comments', on_delete=models.CASCADE)
    creator = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Comment."""  

        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content
        # return "Comment by " + str(self.creator) + " on \"" + str(self.article) + "\""