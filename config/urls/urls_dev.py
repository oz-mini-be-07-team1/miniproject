from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('users/',include('users.urls')),
    path('account/', include('accounts.urls')),
    path('notifications/', include('notifications.urls')),  

    # 거래 내역 관련 API
    path('transaction-history/', include('transaction_history.urls')), 
]

