from django.db import models
from django.contrib.auth.models import User
import random

class UserAuthentication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auth_user')
    code = models.CharField()
