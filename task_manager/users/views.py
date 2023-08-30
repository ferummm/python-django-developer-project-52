from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import RegisterForm
from django.utils.translation import gettext as _

# Create your views here.

class IndexView(View):

    template_name="users/index.html"

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, self.template_name, context={'users': users})
    

class RegistrationFormView(View):
    form_class = RegisterForm
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(auto_id=False)
        
        return render(request, self.template_name, context={'form': form,
                                                    'title': _("Registration")})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,auto_id=False)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration was successful!"))
            return redirect('users')
        return render(request, self.template_name, {'form': form,
                                                    'title': _("Registration")})