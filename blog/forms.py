from django.forms import ModelForm

from blog.models import Post


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'excerpt', 'thumbnail', 'category', 'content']
