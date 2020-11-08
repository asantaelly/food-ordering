from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField


from database.models import *


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput
        )

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        check_email = CustomUser.objects.filter(email=email)
        if check_email.exists():
            raise forms.ValidationError("Email is taken")
        return email

    def clean_confirmed_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords don't match")
        return confirm_password
