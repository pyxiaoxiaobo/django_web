from django.shortcuts import render
from .serializers import BookSerializer, BookModelSerializer, BookModelSerializer2
from .serializers import TypeModelSerializer, Type2ModelSerializer
from .serializers import Type3ModelSerializer, Type4ModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile, Book
from .models import Type, Type2, Type3, Type4
from rest_framework import mixins, generics, viewsets
from rest_framework.permissions import BasePermission
# Create your views here.
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer





class Type1View(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        Types = Type.objects.all()
        types_serializer = TypeModelSerializer(Types, many=True)
        return Response(types_serializer.data)


class Type2View(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, reuqest, format=None):
        Types = Type2.objects.all()
        types_serializer = Type2ModelSerializer(Types, many=True)
        return Response(types_serializer.data)

class Type3View(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        Types = Type3.objects.all()
        types_serializer = Type3ModelSerializer(Types, many=True)
        return Response(types_serializer.data)


class Type4View(APIView):
    renderer_classes = [JSONRenderer]
    def get(self, request, format=None):
        Types = Type4.objects.all()
        types_serializer = Type4ModelSerializer(Types, many=True)
        return Response(types_serializer.data)

class IsDeveloper(BasePermission):
    message = "查无此人"
    def has_permission(self, request, view):
        api_key  = request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(api_key=api_key).first()
        if developer:
            return True
        else:
            print(self.message)
            return False


class EnoughMoney(BasePermission):
    message = "兄弟, 又到了需要充钱的时候！好开心啊！"
    def has_permission(self, request, view):
        api_key = request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(api_key=api_key).first()
        balance = developer.money
        if balance > 0:
            developer.money -= 1
            developer.save()
            return True
        else:
            return False


class BookModelViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    permission_classes =  [IsDeveloper, EnoughMoney]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer2
    def get_queryset(self):
        isbn = self.request.query_params.get('isbn', 0)
        books = Book.objects.filter(isbn=int(isbn))
        queryset = books
        return queryset


class BookMixinView2(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get(self, request, *args, **kwargs):
        api_key = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(api_key=api_key).first()
        if not developer:
            return Response('查无此人')
        balance = developer.money
        if balance <= 0:
            return Response("兄弟，又到了需要充钱的时候！好开心啊！")
        isbn = self.request.query_params.get('isbn', 0)
        developer.money -= 1
        developer.save()
        self.queryset = Book.objects.filter(isbn=int(isbn))
        return self.list(request, *args, **kwargs)


class BookMxinView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    def get(self, request, *args, **kwargs):
        api_key = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(api_key=api_key).first()
        if not developer:
            return Response("查无此人")
        balance = developer.money
        if balance <= 0:
            return Response("兄弟，又到了需要充钱的时候了")
        isbn = self.request.query_params.get('isbn', 0)
        developer.money -= 1
        developer.save()
        self.queryset = Book.objects.filter(isbn=int(isbn))
        return self.list(request, *args, **kwargs)


class BooKAPIView2(APIView):
    '''
    使用ModelSerializer
    '''
    def get(self, request, format=None):
        api_key = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(api_key=api_key).first()
        if not developer:
            return Response('查无此人')
        balance = developer.money
        if balance <= 0:
            return Response("兄弟，又到了充钱的时候! 好开心啊")
        isbn = self.request.query_params.get("isbn", 0)
        books = Book.objects.filter(isbn=int(isbn))
        books_serializer = BookModelSerializer(books, many=True)
        developer.money-=1
        developer.save()
        return Response(books_serializer.data)



class BookAPIView(APIView):
    '''
    使用serializer
    '''
    def get(self, request, format=None):
        api_key = self.request.query_params.get('apikey', 0)
        developer = UserProfile.objects.filter(api_key=api_key).first()
        if developer:
            balance = developer.money
            if balance > 0:
                isbn = self.request.query_params.get('isbn', 0)
                books = Book.objects.filter(isbn=int(isbn))
                books_serializer = BookSerializer(books, many=True)
                developer.money-=1
                developer.save()
                return Response(books_serializer.data)
            else:
                return Response('兄弟，又到充钱的时候了！好开心啊')
        else:
            return Response("查无此人")