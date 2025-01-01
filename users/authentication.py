from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # 쿠키에서 access_token 가져오기
        access_token = request.COOKIES.get("access_token")
        print(f"Access Token: {access_token}")  # 디버깅
        if not access_token:
            print("Access Token not found in cookies.")  # 쿠키에서 토큰 없을 때 로그 추가 
            return None  # 인증 실패

        try:
            # 토큰 유효성 검증
            validated_token = self.get_validated_token(access_token)
            print(f"Validated Token: {validated_token}")
        except Exception as e:
            print(f"Token validation error: {e}")
            return None  # 유효하지 않은 토큰

        try:
            # 유효한 토큰으로 사용자 반환
            user_id = validated_token[api_settings.USER_ID_CLAIM]  # 토큰에서 user_id 추출
            user = self.user_model.objects.get(**{api_settings.USER_ID_FIELD: user_id})  # 기본 키 필드로 조회
        except self.user_model.DoesNotExist:  # 유효하지 않은 사용자 ID 예외 처리 ##
            print(f"User with ID {user_id} does not exist.")
            return None
        except Exception as e:  # 사용자 조회 중 기타 예외 처리
            print(f"Error retrieving user: {e}")
            return None

        return user, validated_token
