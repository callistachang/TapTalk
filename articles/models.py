from django.db import models

# Create your models here.

class Article(models.Model):
    """Model definition for Article."""

    id = models.AutoField(primary_key=True)
    content = models.TextField()
    headline = models.CharField(max_length=150)
    byline = models.TextField(null=True)
    author = models.CharField(max_length=150)
    date_published = models.DateTimeField(auto_now_add=True)
    num_sections = models.IntegerField()
    picture_src = models.URLField(max_length=200)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        pass
