from django.db import models

from sections.models import Section

# Create your models here.

class Article(models.Model):
    """Model definition for Article."""

    id = models.AutoField(primary_key=True)
    byline = models.TextField(null=True, blank=True)
    num_views = models.IntegerField(default=0, blank=True)
    num_shares = models.IntegerField(default=0, blank=True)
    picture_src = models.URLField(max_length=200, null=True, blank=True)

    # Necessary fields
    headline = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    date_published = models.DateField()
    sections = models.ManyToManyField(Section, related_name='article')

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.headline