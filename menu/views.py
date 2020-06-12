from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.views import generic

from .models import Menu
from accounts.models import CustomUser

class IndexView(generic.ListView):
    model = Menu
    context_object_name = 'menu_list'
    template_name = 'menu/menu_list.html'


def create_menu(request):
    context = {
        'title': 'Register your dish here',
    }
    return render(request, 'menu/register.html', context)

def store_menu(request):

    class MenuForm(ModelForm):
        class Meta:
            model = Menu
            fields = ()

    if request.method == "POST":
        form = MenuForm(request.POST, request.FILES)
        if form.is_valid():
            id = 1                  # ID will be represented by the logged-in user
            user = CustomUser.objects.get(pk=id)
            Menu.objects.create(
                title = form.data['title'],
                details = form.data['details'],
                picture = form.files['picture'],
                price = form.data['price'],
                user = user,
            ).save()

            context = {
                'success': True,
                'message': 'Menu was successfullu registered.'
            }
            return redirect('/menu/', context)
        else:
            context = {
                'success': False,
                'message': 'Your form is not valid'
            }
            return redirect('/menu/register/', context)