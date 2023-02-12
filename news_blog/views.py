from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'news_blog/index.html')


def login(request):
    return render(request, 'news_blog/login.html')


def sign_up(request):
    return render(request, 'news_blog/sign_up.html')


def article_view(request):
    return render(request, 'news_blog/article_view.html')


def post_creation(request):
    return render(request, 'news_blog/post_creation.html')


def view_all(request):
    return render(request, 'news_blog/view_all.html')
