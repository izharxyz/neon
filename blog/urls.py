from django.urls import path

from .views import IndexView, PostCreateView, PostDetailView, PostUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/create/', PostCreateView.as_view(), name='post-create'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
]
