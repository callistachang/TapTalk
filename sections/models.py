from django.db import models

# Create your models here.

class Section(models.Model):
    """Model definition for Section."""

    id = models.AutoField(primary_key=True)
    paragraph = models.TextField()

    class Meta:
        """Meta definition for Section."""

        verbose_name = 'Section'
        verbose_name_plural = 'Sections'

    def __str__(self):
        """Unicode representation of Section."""
        return str(self.id)