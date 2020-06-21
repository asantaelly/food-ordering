from django.shortcuts import render, redirect
from django.forms import ModelForm
from django.views import generic

from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Menu
from accounts.models import CustomUser
from .serializers import MenuSerializer

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


# API restful-framework
def menu_list(request):
    
    if request.method == 'GET':
        menu_all = Menu.objects.all()
        serializer = MenuSerializer(menu_all, context={'request': request}, many=True)
        return JsonResponse(serializer.data, safe=False)

@api_view(['POST'])
def menu_create(request):

    if request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)