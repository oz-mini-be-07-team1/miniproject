from django.apps import AppConfig
from django.conf import settings

class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"

    def ready(self):
        from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
        from users.models import User

        OutstandingToken.user.field.remote_field.model = User