from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import RegisterForm

def register_user(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.set_password(form.cleaned_data['confirmed_password'])
            user.save()

            context = {
                'success': True,
                'message': 'Welcome to the service'
            }
            return render(request, 'xxxx/xxx.html', context)
        else:
            context = {
                'success': False,
                'message': 'Please check your input, Something is wrong.'
            }
            return render(request, 'xxxx/xxx.html', context)
    else:
        form = RegisterForm()
        return render(request, 'xxxx/xxx.html', {"form": form})

        