"""taptalk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Please change
    path('auth/facebook', views.facebook_auth, name='facebook_auth'),
    path('auth/linkedin', views.linkedin_auth, name='linkedin_auth'),

    path('article/<int:pk>', views.ArticleView.as_view(), name='article'),
    path('article/<int:article_id>/post_comment', views.post_comment, name='post_comment'),
    path('profile/<int:pk>', views.ProfileView.as_view(), name='profile'),
    path('', views.MainView.as_view(), name='main'),
]
