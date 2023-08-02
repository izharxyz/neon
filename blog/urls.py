from django.urls import path
from .views import IndexView, PostDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('blog/<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
