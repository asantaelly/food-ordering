from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView

from api.menu import rest_api

app_name = 'menu'

urlpatterns = [
    path('', rest_api.menu_list),
    path('<int:pk>', rest_api.menu_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
