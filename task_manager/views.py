from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def ind(request):
    return HttpResponse('<h1>Hello, World!</h1>')


def index(request):
    return render(request, 'index.html')


class LogInView(View):
    template_name = "login.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Logging in failled, try again"))
            return redirect('login')


class LogOutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, ("You were logged out"))
        return redirect('home')


class AboutView(View):
    template_name = "about.html"
    github = "https://github.com/ferummm"
    tg = "https://t.me/ferummm"
    vk = "http://vk.com/ferummm"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,
                      context={'github': self.github,
                               'tg': self.tg,
                               'vk': self.vk})
