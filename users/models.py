from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# django 기본 user model 상속 (커스텀 usera 모델)
class User(AbstractUser):
    pass
