from django.shortcuts import render, redirect
from .models import Post, UserSignUpForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    # template_name = 'news_blog/index.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

# def index(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'news_blog/index.html', context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def login(request):
    return render(request, 'news_blog/login.html', {'title': "Login Page"})


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account Successfully Created for {username} Login Now!')
            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'news_blog/sign_up.html', {
        'form': form,
        'title': "Signup Page"
        })


def article_view(request):
    return render(
        request, 'news_blog/article_view.html', {'title': "Article View"})


# def post_creation(request):
#     return render(
#         request, 'news_blog/post_creation.html', {'title': "Post Creation"})


# def view_all(request):
#     return render(request, 'news_blog/view_all.html', {'title': "All Posts"})


@login_required
def profile(request):
    return render(request, 'news_blog/profile.html')


@login_required
def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
            )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been Updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        "u_form": u_form,
        "p_form": p_form
    }
    return render(request, 'news_blog/profile_update.html', context)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
