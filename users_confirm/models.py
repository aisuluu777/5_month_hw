from django.db import models
from django.contrib.auth.models import User
import random

class UserAuthentication(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='auth_user')
    code = models.CharField(max_length=6, unique=True)

def create_code():
    return ''.join(random.choices('0123456789', k=6))

