from django.shortcuts import render, HttpResponse
from .models import Post

# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'news_blog/index.html', context)


def login(request):
    return render(request, 'news_blog/login.html', {'title': "Login Page"})


def sign_up(request):
    return render(request, 'news_blog/sign_up.html', {'title': "Signup Page"})


def article_view(request):
    return render(
        request, 'news_blog/article_view.html', {'title': "Article View"})


def post_creation(request):
    return render(
        request, 'news_blog/post_creation.html', {'title': "Post Creation"})


def view_all(request):
    return render(request, 'news_blog/view_all.html', {'title': "All Posts"})
