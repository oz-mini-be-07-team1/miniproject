from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

# 알림 목록 조회 및 생성
class NotificationListCreateView(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # 현재 사용자의 알림만 조회
        return Notification.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # 알림 생성 시 사용자 자동 설정
        serializer.save(user=self.request.user)

# 알림 상세 조회 및 삭제
class NotificationDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user)
