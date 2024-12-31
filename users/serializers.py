from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate

# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["email", "password", "name", "nickname", "phone_number"]

    # 이메일 중복 검사
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('이미 사용 중인 이메일입니다.')
        return value
    
    # 닉네임 중복 검사
    def validate_nickname(self, value):
        if User.objects.filter(nickname=value).exists():
            raise serializers.ValidationError('이미 사용 중인 닉네임입니다.')

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            nickname=validated_data['nickname'],
            phone_number=validated_data['phone_number'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user

# 로그인
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError("이메일 또는 비밀번호가 잘못되었습니다.")
        return user
    
# 회원 정보
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ["id", "email", "name", "nickname", "phone_number", "is_staff", "is_active"]


# 회원 정보 수정
class UserUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["name", "nickname", "phone_number"]