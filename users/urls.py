from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import (CheckUsernameExists, PasswordResetView, ProfileView,
                         RegisterView)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(
        template_name='users/login.html',
        redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout'), name='logout'),
    path('check-username-exists/', CheckUsernameExists.as_view(),
         name='check-username-exixts'),
    path('password-reset/', PasswordResetView.as_view(), name='password-reset'),

    path('profile/<slug:username>/', ProfileView.as_view(), name='user-profile')
]
