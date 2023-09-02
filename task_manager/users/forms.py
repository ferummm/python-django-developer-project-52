from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label=_('Email'),
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(required=True,
                                 label=_('First name'),
                                 min_length=1, max_length=50,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                                label=_('Last name'),
                                min_length=1,
                                max_length=50,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = _('Username')

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].label = _('Password')

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].label = _('Password confirmation')
