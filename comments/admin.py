from django.contrib import admin
from .models import Comment

# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_filter = ("article_section__article", "date_posted")
    list_display = ("content", "creator", "article_section", "date_posted")

    # list_filter = ("article__headline", "date_posted")
    # list_display = ("content", "creator", "article", "date_posted")
    pass