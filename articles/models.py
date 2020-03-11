from django.db import models

# Create your models here.

class Article(models.Model):
    """Model definition for Article."""

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    headline = models.CharField(max_length=150)
    byline = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=150)
    date_published = models.DateTimeField()
    num_sections = models.IntegerField(null=True, blank=True) # Update based on content
    picture_src = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.headline
