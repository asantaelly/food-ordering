from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from graphene_django.views import GraphQLView

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list),
    path('<int:pk>', views.menu_detail),
    path("graphql", GraphQLView.as_view(graphiql=True)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
