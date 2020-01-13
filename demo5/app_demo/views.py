from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
# Create your views here.

class IndexView(APIView):
    '''
    首页
    '''
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        'Token a176130c3c0f769c617d687ba9718660e396c0f5'
        return HttpResponse('首页')