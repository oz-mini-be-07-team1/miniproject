from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import PermissionDenied
from django.contrib.auth import authenticate
from .models import User
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UserUpdateSerializer


# 회원가입 api
class SignUpAPIView(APIView):
    permission_classes = [AllowAny] # 누구나 접근 가능하게 해주는 api

    def post(self, request):
        serializer = RegisterSerializer(data=request.data) # 사용자 데이터 검증 및 저장
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 로그인 api
class LoginAPIView(APIView):
    permission_classes = [AllowAny] # 누구나 접근 가능하게 해주는 api

    def post(self, request):
        serializer = LoginSerializer(data=request.data) # 사용자 정보 검증 후 JWT토큰 발급

        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({"access": str(refresh.access_token),
                            "refresh": str(refresh)
                            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 로그아웃 api
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated] # 인증된 사용자만 접근하게 해준다

    def post(self, request):
        refresh_token = request.data.get("refresh")
        try:
            token = RefreshToken(refresh_token)
            token.blacklist() # 이미 발급된 토큰에 대한 접근 제한
            return Response({"message": "로그아웃 되었습니다."}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error":str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

# 회원 정보 조회, 수정, 삭제 api
class UserInfoAPIView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return UserUpdateSerializer
        return UserSerializer
    
    # 본인 계정만 접근 가능하도록 제한
    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.id != self.kwargs['pk']:
            raise PermissionDenied('본인의 정보만 접근할 수 있습니다.')
        return super().get_queryset()
    
    def perform_destroy(self, instance):
        instance.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_200_OK)
