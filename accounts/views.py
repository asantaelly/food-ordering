from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RegisterForm


def index(request):
    context = {
        'title': 'Welcome to the boring site',
    }
    return render(request, 'accounts/index.html', context)


def registration_form(request):
    context = {
        'Success': True,
        'Message': 'Registration form'
    }
    return render(request, 'accounts/register.html', context)


def register_user(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.set_password(form.cleaned_data['confirm_password'])
            user.save()

            context = {
                'success': True,
                'message': 'Welcome to the service'
            }
            return render(request, 'accounts/index.html', context)
        else:
            context = {
                'success': False,
                'message': 'Please check your input, Something is wrong.'
            }
            return render(request, 'accounts/register.html', context)
    else:
        form = RegisterForm()
        return render(request, 'accounts/register.html', {"form": form})

        