"""news URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from news_blog.views import *


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),

    path('', PostListView.as_view(), name="index"),

    path('login/', auth_views.LoginView.as_view(
        template_name='news_blog/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='news_blog/logout.html'), name='logout'),

    path('sign-up/', sign_up, name='sign_up'),

    path('profile/', profile, name='profile'),

    path('profile/profile-update', profile_update, name='profile_update'),

    path('article-view/<int:pk>/', PostDetailView.as_view(
        template_name='news_blog/article_view.html'), name='article_view'),

    path('article-view/<int:pk>/update', PostUpdateView.as_view(template_name='news_blog/post_update.html'), name='post_update'),

    path('post-creation/', PostCreateView.as_view(), name='post_creation'),

    path('article-view/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),

    path('post/<int:pk>/like/', post_like, name='post_like'),

    # path('view-all-posts/', view_all, name='view_all'),
]
