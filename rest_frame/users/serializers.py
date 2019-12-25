from rest_framework import serializers
from .models import UserProfile, Book, Type, Type2, Type3, Type4
from .models import NewType


class NewTypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewType
        fields = "__all__"


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(
        required=True,
        max_length=100,
    )
    isbn = serializers.CharField(
        required=True,
        max_length=100
    )
    author = serializers.CharField(
        required=True,
        max_length=100
    )
    publish = serializers.CharField(
        required=True,
        max_length=100
    )
    rate = serializers.FloatField(default=0)

class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # 将整个表序列化
        fields = "__all__"

class BookModelSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Book
        # 指定序列化
        fields = ('title', 'isbn', 'author')


class TypeModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'


class Type2ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type2
        fields = '__all__'


class Type3ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type3
        fields = '__all__'


class Type4ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type4
        fields = '__all__'
