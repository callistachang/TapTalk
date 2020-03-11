from django.contrib import admin

from .models import User, Expert

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_filter = ('is_expert',)

class ExpertAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_verified', 'expert_title')

admin.site.register(User, UserAdmin)
admin.site.register(Expert, ExpertAdmin)

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass

from django.contrib.auth.models import User as DefaultUser
from django.contrib.auth.models import Group

admin.site.unregister(DefaultUser)
admin.site.unregister(Group)