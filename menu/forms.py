from django import forms

from menu.models import Menu

class MenuForm(forms.ModelForm):

    class Meta:
        model = Menu
        fields = ("title", "details", "price", "picture", "is_available")