# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status, generics
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.contrib.auth import authenticate
# from .models import User
# from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UserUpdateSerializer


# # 회원가입 api
# class SignUpAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "회원가입이 완료되었습니다."}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# # 로그인 api
# class LoginAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data
#             refresh = RefreshToken.for_user(user)
#             return Response({"access": str})
