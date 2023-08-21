from django.urls import path

from .views import (CategoryView, IndexView, PostCreateView, PostDeleteView,
                    PostDetailView, PostSearchView, PostUpdateView)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/search/', PostSearchView.as_view(), name='post-search'),

    path('blog/create/', PostCreateView.as_view(), name='post-create'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
    path('blog/update/<slug:slug>/', PostUpdateView.as_view(), name='post-update'),
    path('blog/delete/<slug:slug>/', PostDeleteView.as_view(), name='post-delete'),
    path('blog/category/<slug:slug>/', CategoryView.as_view(), name='category'),

]
