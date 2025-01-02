from django.urls import path
from .views import (
    AccountCreateView, AccountDetailView, AccountDeleteView,
)

# 하이픈(-): url이나 파일명, SEO 즉 사람의 가독성이 필요로 할 때 사용 됨/ 프로그래밍 언어에서는 minus 로 사용 되기 때문에 X
# 언더바(_): 프로그래밍 언어의 변수명이나 함수, 클래스명으로 사용
urlpatterns = [
    path('', AccountCreateView.as_view(), name='account-create'),
    path('<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),
]
