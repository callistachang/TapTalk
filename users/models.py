from django.db import models

from articles.models import Article

class User(models.Model):
    """Model definition for User."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    picture_src = models.URLField(null=True, blank=True, max_length=200)
    saved_articles = models.ManyToManyField(Article, blank=True)
    is_expert = models.BooleanField(default=False)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        return self.name

        
class Expert(User):
    """Model definition for Expert."""

    is_verified = models.BooleanField(default=False)
    expert_title = models.CharField(max_length=150)

    class Meta:
        """Meta definition for Expert."""

        verbose_name = 'Expert'
        verbose_name_plural = 'Experts'

    def __str__(self):
        """Unicode representation of Expert."""
        return self.name