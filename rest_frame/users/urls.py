from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('apibook5', BookModelViewSet)

urlpatterns = [
    path('apibook/', BookAPIView.as_view(), name='book1'),
    path('apibook2/', BooKAPIView2.as_view(), name='book2'),
    path('apibook3/', BookMxinView.as_view(), name='book3'),
    path('apibook4/', BookMixinView2.as_view(), name='book4'),
    path('', include(router.urls)),
    path('type/', Type1View.as_view()),
    path('type2/', Type2View.as_view()),
    path('type3/', Type3View.as_view()),
    path('type4/', Type4View.as_view()),
]
