from django.db import models
from common.models import CommonModel

class User(CommonModel):
    user_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    last_login = models.DateTimeField(null=True, blank=True) # null, blank = True 로 비어 있는 값 허용
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'users' # 보기 쉽게 이름 지정

    def __str__(self):
        return self.email