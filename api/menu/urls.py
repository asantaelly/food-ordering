from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt

from api.menu import rest_api

app_name = 'menu'

urlpatterns = [
    path('', csrf_exempt(jwt_cookie(rest_api.menu_list))),
    path('<int:pk>', rest_api.menu_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
