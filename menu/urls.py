from django.urls import path

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.create_menu, name='create_menu'),
]
