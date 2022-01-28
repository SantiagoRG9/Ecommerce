from turtle import mode
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer, UpdateUserSerializer
from rest_framework.decorators import api_view

class UserViewSet(viewsets.GenericViewSet):
    model = User
    serializer_class = UserSerializer
    list_serializer_class = UserListSerializer

    def get_object(self, pk):
        return get_object_or_404(self.serializer_class.Meta.model, pk=pk)


    def list(self, request):
        users = User.objects.all().values('id','username','email','name')
        users_serializer = self.list_serializer_class(users, many = True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        user_serializer = self.serializer_class(data = request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message' : 'Usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({
            'message' : 'Hay errores en el registro',
            'errors' : user_serializer.errors
        },status= status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)

    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message' : 'Usuario actualizado correctamente!'
            }, status= status.HTTP_200_OK)
        return Response({
            'message' : 'Hay errores en la actualizacion',
            'errors' : user_serializer.errors
        },status = status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id = pk).update(is_active=False)
        if user_destroy == 1:
            return Response({
                'message' : 'Usuario Eliminado correctamente!'
            })
        return Response({
            'message' : 'No existe el usuario que desea eliminar!'
        }, status = status.HTTP_404_NOT_FOUND)

        
