from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse
from cloudinary.models import CloudinaryField
from cloudinary.uploader import upload
from django.contrib.auth import get_user_model
# from .forms import CommentForm

# Create your models here.

# class Post(models.Model):
#     title = models.CharField(max_length=70)
#     content = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)

# def __str__(self):
#     return self.title

# def get_absolute_url(self):
#     return reverse('article_view', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, through='Like')
    image = CloudinaryField(
        'image', folder='media/post_pics/', null=True, blank=True, default='https://res.cloudinary.com/ddfkccacb/image/upload/t_Grayscale/v1675254029/media/post_pics/sample.jpg', transformation=[{'width': 500, 'height': 500, 'crop': 'limit'}])

    # def save(self, *args, **kwargs):
    #     if self.image and not self.image.name.startswith('http'):
    #         # Use CloudinaryUploader to upload the image to Cloudinary
    #         uploaded = upload(self.image, folder='media/post_pics/', transformation=[{"width": 1000, "height": 1000, "crop": "limit"}])
    #         self.image = uploaded['secure_url']
    #     super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_view', kwargs={'pk': self.pk})


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='media/profile_pics/default_image_wude5m.jpg', upload_to='media/profile_pics/')
    image = CloudinaryField(
        'image', folder='media/post_pics/', null=True, blank=True, default='media/profile_pics/vsquvarj1tbivkaoe1vr.jpg', transformation=[{'width': 500, 'height': 500, 'crop': 'limit'}])

    def __str__(self):
        return f'{self.user.username} Profile'


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
