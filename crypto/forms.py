from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Enter Username"
    }))

    password = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Enter Password"
    }))

    class Meta:
        model = User
        fields = ("username", "password")

    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user


class NewUserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "text",
        "placeholder": "Enter Username"
    }))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "email",
        "placeholder": "Enter Your Email"
    }))
    password1 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Enter Password",
    }))
    password2 = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class": "form-control",
        "type": "password",
        "placeholder": "Confirm Password"
    }))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email'],
        user.username = self.cleaned_data['username']
        if commit:
            user.save()
        return user
