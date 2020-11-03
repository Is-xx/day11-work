from rest_framework.response import Response
from rest_framework.views import APIView


class UserAPIView(APIView):

    def get(self, request, *args, **kwargs):
        print('读请求')
        return Response('读ok')

    def post(self, request, *args, **kwargs):
        print('写请求')
        return Response('写ok')

