from django.shortcuts import render
from django.views import View
from blog.models import Post


class IndexView(View):
    def get(self, request):
        featured_post = Post.objects.order_by('-views').first()
        posts = Post.objects.all().exclude(id=featured_post.id)
        return render(request, 'blog/index.html', {'featured_post': featured_post, 'posts': posts})
