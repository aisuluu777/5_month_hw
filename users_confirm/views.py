from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist

from . import serializers, models
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import create_code, UserAuthentication


@api_view(['POST'])
def authorization_api_view(request):
    serializer = serializers.UserAuthenticateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(data={'token': token.key}, status=status.HTTP_200_OK)
    return Response(data={'Неправильные данные, попробуйте снова'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def register_api_view(request):
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


@api_view(['POST'])
def activate_user_api_view(request):
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





