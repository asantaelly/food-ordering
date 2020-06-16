from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('register/', views.create_menu, name='create_menu'),
    path('store/', views.store_menu, name='store_menu'),
    path('list', views.menu_list, name='menu_list'),
]
