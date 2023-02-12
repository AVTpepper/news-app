from django.shortcuts import render, HttpResponse

# Create your views here.


posts = [
    {
        'author': 'Alex T',
        'title': 'News Post 1',
        'content': 'This is my first news post',
        'date_posted': '11th September, 2023'
    },
    {
        'author': 'Evelina E',
        'title': 'News Post 2',
        'content': 'This is my second news post',
        'date_posted': '3rd November, 2023'
    },
]


def index(request):
    context = {
        'posts': posts
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
