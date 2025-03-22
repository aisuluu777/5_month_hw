from rest_framework import serializers
from django.contrib.auth.models import User

class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=20)
    email = serializers.EmailField(min_length=3, max_length=50)
    password = serializers.CharField(min_length=8, max_length=50)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except:
            return username
        raise serializers.ValidationError('Username already taken')

class UserAuthenticateSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=3, max_length=20)
    password = serializers.CharField(min_length=8, max_length=50)
