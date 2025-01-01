from django.urls import path
from .views import (
    AccountCreateView, AccountDetailView, AccountDeleteView,
)

urlpatterns = [
    path('', AccountCreateView.as_view(), name='account-create'),
    path('<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('<int:pk>/delete/', AccountDeleteView.as_view(), name='account-delete'),
]
