from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from .forms import UserRegisterForm


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('index')
        else:
            return render(request, 'users/register.html', {'form': form})
