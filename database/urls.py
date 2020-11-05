from django.urls import path

from . import views

app_name = 'database'


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.registration_form, name='register'),
    path('registering', views.register_user, name='registering')
]
