from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from . import serializers, models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import create_code, UserAuthentication
from rest_framework.views import APIView


class AuthorizationApiView(APIView):
    def post(self, request):
        serializer = serializers.UserAuthenticateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            token, _ = Token.objects.get_or_create(user=user)
            return Response(data={'token': token.key}, status=status.HTTP_200_OK)
        return Response(data={'Неправильные данные, попробуйте снова'}, status=status.HTTP_400_BAD_REQUEST)



class RegisterApiView(APIView):
    def post(self, request):
        serializer = serializers.UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        password = serializer.validated_data.get('password')
        user = User.objects.create_user(username=username,
                                 email=email, password=password, is_active=False)
        code = create_code()
        print(code)
        UserAuthentication.objects.create(user=user, code=code)
        return Response(data={'user_id' : user.id}, status=status.HTTP_201_CREATED)


class ConfirmApiView(APIView):
    def post(self, request):
        code = request.data.get('code')
        try:
            user_auth = UserAuthentication.objects.get(code=code)
            user = user_auth.user
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if user_auth.code == code:
            user.is_active = True
            user.save()
            return Response(data={'Ваш аккаунт успешно активирован'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'Неправильный код'}, status=status.HTTP_400_BAD_REQUEST)








# class EmailApiView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         try:
#             user = User.objects.get(email=email)
#             code = UserAuthentication.objects.get(user=user)
#
#             send_mail(
#                 'ваш код',
#                 f'Ваш код сброса пароля: {code.code}',
#                 'aisuluunurlanova@gmail.com',
#                 [email],
#                 fail_silently=False,
#             )
#             return Response(status=status.HTTP_200_OK)
#         except User.DoesNotExist:
#             return Response("Пользователь с таким email не найден.")





