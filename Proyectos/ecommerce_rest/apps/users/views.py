from datetime import datetime
from django.contrib.sessions.models import Session

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


# ------------ IMPORTACIONES 2 MANERA ------
# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token

# from apps.users.authentication_mixins import Authentication
# from apps.users.api.serializers import UserTokenSerializer

#------------------------ LOGIN LOGOUT CON SIMPLE JWT MANERA RECOMENDADA ------------------------------------
from apps.users.api.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer
from apps.users.models import User

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import GenericAPIView

from django.contrib.auth import authenticate

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username = username,
            password = password
        )

        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token' : login_serializer.validated_data.get('access'),
                    'refresh-token' : login_serializer.validated_data.get('refresh'),
                    'user' : user_serializer.data,
                    'message' : 'Inicio de sesion Exitoso'
                }, status = status.HTTP_200_OK)

            return Response({'error' : 'Contraseña o nombre de usuario incorrectos'},status = status.HTTP_400_BAD_REQUEST)
        return Response({'error' : 'Contraseña o nombre de usuario incorrectos'},status = status.HTTP_400_BAD_REQUEST)


class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user',0))          # ENVIAR ID DE USUARO
        if user.exists():                                                  # VALIDAR SI EXISTE
            RefreshToken.for_user(user.first())                            # REFRESCAR EL TOKEN QUE SE UTILIZA
            return Response({'message' : 'Sesion cerrada correctamente'},status = status.HTTP_200_OK)
        return Response({'error' : 'No existe este usuario'},status = status.HTTP_400_BAD_REQUEST)

"""
                                ESTOS LOGIN Y LOGOUT SE PUEDEN COMPLEMENTAR CON 
                                MAS COSAS VISTAS EN EL LOGIN MANERA #2
                                                    """





# ------------------------------ LOGIN & LOGOUT 2 MANERA ------------------------


# class UserToken(Authentication,APIView):
#     """
#     Validate Token
#     """
#     def get(self, request, *args, **kwargs):
#         try:
#             user_token,_ = Token.objects.get_or_create(user = self.user)
#             user = UserTokenSerializer(self.user)
#             return Response({
#                 'token' : user_token.key,
#                 'user' : user.data
#             })
#         except:
#             return Response({
#                 'error' : 'Credenciales enviadas incorrectas'
#             },status = status.HTTP_400_BAD_REQUEST)

# class Login(ObtainAuthToken):
    
#     def post(self,request,*args,**kwargs):
#         login_serializer = self.serializer_class(data = request.data, context = {'request':request})
#         if login_serializer.is_valid():
#             user = login_serializer.validated_data['user']
#             if user.is_active:
#                 token,created = Token.objects.get_or_create(user = user)
#                 user_serializer = UserTokenSerializer(user)
#                 if created:
#                     return Response({
#                         'token' : token.key,
#                         'user' : user_serializer.data,
#                         'message' : 'Inicio de Sesion exitoso'
#                     },status =status.HTTP_201_CREATED)
#                 else:
                    
#                     all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
#                     if all_sessions.exists():
#                         for session in all_sessions:
#                             session_data = session.get_decoded()
#                             if user.id == int(session_data.get('_auth_user_id')):
#                                 session.delete()
#                     token.delete()
#                     token = Token.objects.create(user = user)
#                     return Response({
#                         'token' : token.key,
#                         'user' : user_serializer.data,
#                         'message' : 'Inicio de Sesion exitoso'
#                     },status =status.HTTP_201_CREATED)
                
#                     """
#                     return Response({
#                         'error': 'Ya se ha iniciado sesion con este usuario'
#                     },status = status.HTTP_409_CONFLICT)
#                     """
              
#             else:
#                 return Response({'error':'Este usuario no puede iniciar sesion'},status=status.HTTP_401_UNAUTHORIZED)
#         else:
#             return Response({'error':'Nombre de usuario o contraseña incorrectos'},status=status.HTTP_400_BAD_REQUEST)
        


# class Logout(APIView):
#     # LA PETICION TIENE QUE SER ENVIADA POR --POST-- AQUI ES POR --GET-- COMO EJEMPLO
#     def get(self, request, *args, **kwargs):

#         try:
#             token = request.GET.get('token')
#             token = Token.objects.filter(key = token).first()
#             if token:
#                 user = token.user

#                 all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
#                 if all_sessions.exists():
#                     for session in all_sessions:
#                         session_data = session.get_decoded()
#                         if user.id == int(session_data.get('_auth_user_id')):
#                             session.delete()

#                 token.delete()
                
#                 session_message = 'Sesiones de usuario eliminadas.'
#                 token_message = 'Token eliminado.'
#                 return Response({'token_message' : token_message,'session_message':session_message}, status =status.HTTP_200_OK)
#             return Response({'error' : 'No se ha encontrado un usuario con estas credenciales'}, status = status.HTTP_400_BAD_REQUEST)
        
#         except:
#             return Response({'error': 'No se ha encontrado token en la peticion'}, status = status.HTTP_409_CONFLICT)