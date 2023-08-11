from django.contrib.auth.models import User
from django.db import models

from blog.models import Post


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(
        max_length=128, null=True, blank=True, default='No Name')
    title = models.CharField(max_length=128, null=True,
                             blank=True, default='enthusiast')
    profile_pic = models.ImageField(
        upload_to='user/profiles', default='user/profiles/default')
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
