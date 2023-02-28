from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from .forms import CommentForm
from django.core.paginator import Paginator


def handle_not_found(request, exception):
    return render(request, 'news_blog/not-found.html')


# Create your views here.


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    paginate_by = 6
    template_name = 'news_blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['most_liked_posts'] = Post.objects.order_by('-likes')[:4]
        return context


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = self.get_object()
        comments = Comment.objects.filter(post=post)

        context['num_likes'] = post.like_set.count()
        context['liked_by_user'] = post.like_set.filter(
            user=self.request.user).exists()
        context['comment_form'] = CommentForm()
        context['comments'] = comments
        return context


@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('article_view', pk=post.pk)
    else:
        form = CommentForm()
    comments = post.comments.all()
    return render(
        request, 'article_view.html', {
            'form': form, 'post': post, 'comments': comments})


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'image']

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
                request,
                f'Account Successfully Created for {username} Login Now!'
                )

            return redirect('login')
    else:
        form = UserSignUpForm()
    return render(request, 'news_blog/sign_up.html', {
        'form': form,
        'title': "Signup Page"
        })


@login_required
def profile(request):
    user = request.user
    user_posts = user.post_set.all().order_by('-date_posted')

    paginator = Paginator(user_posts, 3)
    page = request.GET.get('page')
    user_posts = paginator.get_page(page)

    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user': user,
        'u_form': u_form,
        'p_form': p_form,
        'user_posts': user_posts
        }

    return render(request, 'news_blog/profile.html', context)


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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'image']

    def form_valid(self, form):
        image = form.cleaned_data['image']
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes.add(request.user)
    return redirect('article_view', pk=post.pk)


@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes.remove(request.user)
    return redirect('article_view', pk=post.pk)


@login_required
def all_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    else:
        posts = Post.objects.all()
    return render(
        request, 'news_blog/all_posts.html', {'posts': posts, 'query': query})
