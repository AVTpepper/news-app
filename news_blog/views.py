from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return render(request, 'news_blog/news_blog.html')


def login(request):
    return HttpResponse("<h1> Its working Login</h1>")


def sign_up(request):
    return HttpResponse("<h1> Its working Sign up!</h1>")


def article_view(request):
    return HttpResponse("<h1> Its working view the article</h1>")


def post_creation(request):
    return HttpResponse("<h1> Its working create a post!</h1>")


def view_all(request):
    return HttpResponse("<h1> Its working view all the posts!</h1>")
