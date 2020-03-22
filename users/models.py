from django.db import models

from articles.models import Article

class User(models.Model):
    """Model definition for User."""

    name = models.CharField(max_length=100)
    biography = models.TextField(null=True, blank=True)
    is_taptalk_mode_on = models.BooleanField(default=True, blank=True)

    class Meta:
        """Meta definition for User."""

        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        return self.name

class CommonUser(User):
    """Model definition for CommonUser, a subclass of User."""

    facebook_id = models.CharField(max_length=50, primary_key=True)
    saved_articles = models.ManyToManyField(Article, related_name='users_who_saved', blank=True)

    class Meta:
        """Meta definition for CommonUser."""

        verbose_name = 'CommonUser'
        verbose_name_plural = 'CommonUsers'

    def __str__(self):
        """Unicode representation of CommonUser."""
        return self.name
        
class Expert(User):
    """Model definition for Expert, a subclass of User."""

    email = models.EmailField(max_length=254, primary_key=True)
    is_verified = models.BooleanField(default=False)
    expert_title = models.CharField(max_length=200)
    saved_articles = models.ManyToManyField(Article, related_name='experts_who_saved', blank=True)

    class Meta:
        """Meta definition for Expert."""

        verbose_name = 'Expert'
        verbose_name_plural = 'Experts'

    def __str__(self):
        """Unicode representation of Expert."""
        return self.name