from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import HttpResponse, get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView

from blog.forms import PostCreationForm
from blog.models import Category, Post
from users.models import Profile


class IndexView(View):
    def get(self, request):
        featured_post = Post.objects.order_by('-views').first()
        trending_posts = Post.objects.order_by(
            '-views').exclude(id=featured_post.id)[:5]
        random_posts = Post.objects.order_by(
            '?').exclude(id=featured_post.id)[:12]
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
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Blog post created successfully')
            return redirect('post-detail', post.slug)
        messages.error(request, 'There were errors in form')
        return render(request, 'blog/form.html', {'form': form})


class PostDetailView(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        post.views = post.views + 1
        post.save()

        related_posts = Post.objects.filter(
            category=post.category).exclude(slug=slug)[:5]
        profile = get_object_or_404(Profile, user=post.author)

        ctx = {
            'post': post,
            'profile': profile,
            'related_posts': related_posts
        }
        return render(request, 'blog/detail.html', ctx)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostCreationForm
    template_name = 'blog/form.html'

    def test_func(self):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return self.request.user == post.author

    def get_success_url(self):
        messages.success(self.request, 'Blog post updated successfully')
        slug = self.kwargs['slug']
        return reverse_lazy('post-detail', kwargs={'slug': slug})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete.html'

    def test_func(self):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return self.request.user == post.author

    def get_success_url(self):
        messages.success(self.request, 'Blog post deleted successfully')
        return reverse_lazy('index')
