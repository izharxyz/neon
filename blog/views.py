from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from blog.models import Category, Post
from .forms import PostCreationForm


class IndexView(View):
    def get(self, request):
        featured_post = Post.objects.order_by('-views').first()
        trending_posts = Post.objects.all().exclude(id=featured_post.id)[:5]
        random_posts = Post.objects.order_by(
            '?').exclude(id=featured_post.id)[:9]
        categories = Category.objects.order_by('name')

        ctx = {
            'featured_post': featured_post,
            'trending_posts': trending_posts,
            'random_posts': random_posts,
            'categories': categories
        }
        return render(request, 'blog/index.html', ctx)


class PostCreateView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostCreationForm()
        return render(request, 'blog/form.html', {'form': form})

    def post(slef, request):
        form = PostCreationForm()
        return render(request, 'blog/form.html', {'form': form})


class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        return render(request, 'blog/detail.html', {'post': post})
