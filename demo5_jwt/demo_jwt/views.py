from django.shortcuts import render, redirect, HttpResponse
from rest_framework.views import APIView
# Create your views here.

class IndexView(APIView):
    '''
    首页
    '''

    authentication_classes = []
    permission_classes = []

    def get(self, reuqest):
        return HttpResponse('首页')