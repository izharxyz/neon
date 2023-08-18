from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.text import slugify

from users.models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = slugify(self.cleaned_data['username'])
        if not len(username) > 2:
            raise ValidationError(
                'Username too short.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        valid_email_providers = ('gmail.com', 'protonmail.com', 'pm.me',
                                 'yahoo.com', 'myyahoo.com', 'outlook.com', 'hotmail.com')
        if not email.endswith(valid_email_providers):
            raise ValidationError(
                'Please use reputated email provider like gmail or yahoo.')
        return email


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'title',
                  'bio', 'twitter', 'instagram', 'github']
