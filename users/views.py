from django.shortcuts import HttpResponse, redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.views import View
from .forms import UserRegisterForm


class RegisterView(View):
    def get(self, request):

        try:
            user = User.objects.get(username=request.user.username)
            if user:
                return redirect('index')
        except:
            form = UserRegisterForm()
            return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
        else:
            return render(request, 'users/register.html', {'form': form})


class CheckUsernameExists(View):
    def post(self, request):
        username = request.POST.get('username')

        if not len(username) > 2:
            return HttpResponse('<small style="color: red; padding-left: 4px">username too short</small>')
        else:
            invalid_chars = [' ', '!', '@', '#', '$',
                             '^', '&', '*', '(', ')', '-', '=', '+']
            if any(char in invalid_chars for char in username.strip()):
                return HttpResponse('<small style="color: red; padding-left: 4px">invalid username</small>')
            user = User.objects.filter(username=username.strip()).exists()
            if user:
                return HttpResponse('<small style="color: red; padding-left: 4px">username already taken</small>')

            else:
                return HttpResponse('<small style="color: green; padding-left: 4px">username avlaible</small>')


class PasswordResetView(View):
    def get(self, request):
        messages.error(request, 'mujhe bhi nhi pata, tu gaand mara!')
        return redirect('login')
