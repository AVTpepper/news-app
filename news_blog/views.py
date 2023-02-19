from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, UserSignUpForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View


# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    ordering = ["-date_posted"]
    template_name = 'news_blog/index.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['num_likes'] = post.like_set.count()
        context['liked_by_user'] = post.like_set.filter(user=self.request.user).exists()
        return context


# class PostLike(View):
#     def post(self, request, pk):
#         post = get_object_or_404(Post, pk=pk)
#         if post.like_set.filter(user=request.user).exists():
#             post.like_set.filter(user=request.user).delete()
#         else:
#             Like.objects.create(post=post, user=request.user)
#         return redirect('article-view', pk=pk)

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


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
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
    return HttpResponse('Post liked!')
