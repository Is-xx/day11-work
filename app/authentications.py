from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

from app.models import User


class MyAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION')
        if auth is None:
            return None
        auth_split = auth.split()
        if not (len(auth_split) == 2 and auth_split[0].lower() == 'lxzb'):
            raise exceptions.AuthenticationFailed('格式认证失败')
        if auth_split[1] != 'haohaoxuexi':
            raise exceptions.AuthenticationFailed('信息认证失败')
        user = User.objects.filter(username='admin').first()
        if not user:
            raise exceptions.AuthenticationFailed('用户不存在')
        return user, None
