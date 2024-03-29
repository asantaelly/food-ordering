from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from graphql_jwt.shortcuts import get_token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication


from database.models import Menu
from database.models import CustomUser
from .serializers import MenuSerializer

@api_view(['GET', 'POST'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
def menu_list(request, format=None):
    
    if request.method == 'GET':
        menu_all = Menu.objects.all()
        serializer = MenuSerializer(menu_all, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        if request.user.is_authenticated:
            # token = get_token(request.user)
            # return print(request.auth)
            request.data['user'] = request.user.id
            serializer = MenuSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        

@api_view(['GET', 'PUT', 'DELETE'])
def menu_detail(request, pk, format=None):

    try:
        menu = Menu.objects.get(pk=pk)
    except Menu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)