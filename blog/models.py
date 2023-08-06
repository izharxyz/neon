from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, null=False)
    image = models.ImageField(
        upload_to='static/images/category/', default='static/images/category/default.webp')

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, default='post title')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, max_length=255)
    excerpt = models.CharField(
        max_length=255, null=False, default='an amazing must read post')
    thumbnail = models.ImageField(upload_to='static/images/thumbnails/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)

    content = RichTextUploadingField()

    views = models.IntegerField(default=1)
    likes = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
