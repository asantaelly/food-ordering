from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list),
    path('<int:pk>', views.menu_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
