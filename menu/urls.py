from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.MenuList.as_view()),
    path('<int:pk>', views.MenuDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
