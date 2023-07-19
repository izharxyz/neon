from django.shortcuts import render
from django.views import View
from blog.models import Post


class IndexView(View):
    def get(self, request):
        featured_post = Post.objects.order_by('-views').first()
        trending_posts = Post.objects.all().exclude(id=featured_post.id)[:5]
        return render(request, 'blog/index.html', {'featured_post': featured_post, 'trending_posts': trending_posts})
