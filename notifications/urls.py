from django.urls import path
from .views import NotificationListCreateView, NotificationDetailView

urlpatterns = [
    path('', NotificationListCreateView.as_view(), name='notification-list-create'),  # 알림 목록 및 생성
    path('<int:pk>/', NotificationDetailView.as_view(), name='notification-detail'),  # 알림 상세조회 및 삭제
]
