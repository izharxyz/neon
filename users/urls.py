from django.contrib.auth.views import (LogoutView, PasswordResetCompleteView,
                                       PasswordResetConfirmView,
                                       PasswordResetDoneView,
                                       PasswordResetView)
from django.urls import include, path

from users.views import (CheckUsernameExists, CustomLoginView,
                         ProfileRedirectView, ProfileUpdateView, ProfileView,
                         RegisterView, SubscribeView)

urlpatterns = [

    # social login using social-auth-app-django
    path('social/', include('social_django.urls', namespace='social')),

    # custom auth views
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout'), name='logout'),
    path('check-username-exists/', CheckUsernameExists.as_view(),
         name='check-username-exixts'),

    # password reset
    path('password-reset/', PasswordResetView.as_view(
        template_name='password_reset/email_form.html'), name='password-reset'),
    path('password-reset/email-sent/', PasswordResetDoneView.as_view(
        template_name='password_reset/email_sent.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='password_reset/confirm_form.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='password_reset/complete.html'), name='password_reset_complete'),

    # profile
    path('profile/', ProfileRedirectView.as_view(),
         name='profile'),  # redirect to user-profile
    path('profile/<slug:username>/', ProfileView.as_view(), name='user-profile'),
    path('profile/<slug:username>/update/',
         ProfileUpdateView.as_view(), name='user-profile-update'),

    # subscribe to newsletter
    path('subscribe-newsletter/', SubscribeView.as_view(),
         name='subscribe-newsletter'),
]
