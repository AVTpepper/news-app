from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django import forms

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=70)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
