# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# 장고가 제공하는 기본적인 auth_user table과 연동되는 클래스를 사용
class UserModel(AbstractUser):
    # Meta Class : DB 테이블의 이름을 지정
    class Meta:
        db_table = "user"
