# Generated by Django 3.2.17 on 2023-02-24 16:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news_blog', '0002_auto_20230224_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(
                blank=True, related_name='likes', through='news_blog.Like',
                to=settings.AUTH_USER_MODEL),
        ),
    ]
