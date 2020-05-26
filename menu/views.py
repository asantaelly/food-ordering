from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Its all about the foodie',
    }
    return render(request, 'menu/index.html', context)


def create_menu(request):
    context = {
        'title': 'Register your dish here',
    }
    return render(request, 'menu/register.html', context)