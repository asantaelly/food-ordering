from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from .models import *


class RegisterForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirmed_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
        )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        check_email = CustomUser.users.filter(email=email)
        if check_email.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean_confirmed_password(self):
        password = self.cleaned_data.get("password")
        confirmed_password = self.cleaned_data.get("confirmed_password")
        if password and confirmed_password and password != confirmed_password:
            raise forms.ValidationError("Passwords don't match")
        return confirmed_password
