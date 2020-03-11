from django.contrib import admin
from .models import Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_filter = ("article__headline", "date_posted")
    list_display = ("content", "creator", "article", "date_posted")


admin.site.register(Comment, CommentAdmin)