from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from common.models import CommonModel  # CommonModel 가져오기

# 사용자 정의 매니저 추가
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("이메일은 필수입니다.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("슈퍼유저는 is_staff=True여야 합니다.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("슈퍼유저는 is_superuser=True여야 합니다.")

        return self.create_user(email, password, **extra_fields)

## 기존 User 모델 수정
class User(AbstractBaseUser, PermissionsMixin, CommonModel):  
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, null=True, blank=True)  # 선택적 필드 유지
    phone_number = models.CharField(max_length=20)
    last_login = models.DateTimeField(null=True, blank=True)  # 비어 있는 값 허용
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()  ## 사용자 정의 매니저 연결

    USERNAME_FIELD = 'email'  ## AbstractBaseUser 필수 설정
    REQUIRED_FIELDS = ['name']  ## 이메일 외 추가 필수 필드

    class Meta:
        db_table = 'users'  # 보기 쉽게 이름 지정

    def __str__(self):
        return self.email

    @property
    def id(self):  ## 유지
        return self.user_id
