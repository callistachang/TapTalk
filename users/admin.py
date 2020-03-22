from django.contrib import admin

from .models import CommonUser, Expert

@admin.register(CommonUser)
class CommonUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    # list_display = ('name', 'is_verified', 'expert_title')
    pass

from django.contrib.auth.models import User as DefaultUser
from django.contrib.auth.models import Group

admin.site.unregister(DefaultUser)
admin.site.unregister(Group)