from django.contrib.auth.models import User
from django.db import models

from blog.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='static/images/profiles', default='static/images/profiles/default.webp')
    bio = models.CharField(max_length=1000, null=True, blank=True)

    github = models.URLField(null=True, blank=True, max_length=64)
    instagram = models.URLField(null=True, blank=True, max_length=64)
    twitter = models.URLField(null=True, blank=True, max_length=64)

    """ followers = models.ManyToManyField()
    follows = models.ManyToManyField(Post)

    bookmarks = models.ManyToManyField(Post)
    liked_posts = models.ManyToManyField(Post)
    comments = models.ManyToManyField(Post) """

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"
