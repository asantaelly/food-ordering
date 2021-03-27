from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from graphene_django.views import GraphQLView
from graphql_jwt.decorators import jwt_cookie
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('menu/', include('api.menu.urls')),
    path("graphql", csrf_exempt(jwt_cookie(GraphQLView.as_view(graphiql=True))))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
