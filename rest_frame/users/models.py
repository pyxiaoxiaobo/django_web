from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class NewType(models.Model):
    '''
    商品类别
    '''
    CATEGORY_TYPE = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
        (4, '四级类目'),
    )
    name = models.CharField(
        default='',
        max_length=30,
        verbose_name='类别名',
        help_text='类别名'
    )
    code = models.CharField(
        default='',
        max_length=30,
        verbose_name='类别code',
        help_text='类别code'
    )
    desc = models.CharField(
        default='',
        max_length=30,
        verbose_name='类别描述',
        help_text='类别描述'
    )
    category_type = models.IntegerField(
        choices=CATEGORY_TYPE,
        verbose_name='类别描述',
        help_text='类别描述'
    )
    parent_category = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        verbose_name='父类目录',
        help_text='父类别',
        related_name='sub_cat',
        on_delete=models.CASCADE
    )


class UserProfile(AbstractUser):
    api_key = models.CharField(max_length=30, verbose_name='api_key'
                               , default='abcdefghigklmn')
    money = models.IntegerField(default=10, verbose_name='余额')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Book(models.Model):
    title = models.CharField(max_length=30, verbose_name='书名',
                             default='')
    isbn = models.CharField(max_length=30, verbose_name='isbn',
                            default='')
    author = models.CharField(max_length=20, verbose_name='作者',
                              default='')
    publish = models.CharField(max_length=30, verbose_name='出版社',
                               default='')
    rate = models.FloatField(default=0, verbose_name='豆瓣评分')
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name='添加时间')

    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


from datetime import datetime


class Type(models.Model):
    '''
    一级目录
    '''
    name = models.CharField(max_length=10, default="", verbose_name="类目名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Type2(models.Model):
    '''
    二级目录
    '''
    parent = models.ForeignKey(
        Type,
        verbose_name='父级类别',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=10,
        default='',
        verbose_name='类目名'
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name='添加时间'
    )

    class Meta:
        verbose_name = '商品类别',
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Type3(models.Model):
    '''
    四级类目
    '''
    parent = models.ForeignKey(
        Type2,
        verbose_name='父级类别',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=10,
        default='',
        verbose_name='类目名'
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name='添加时间'
    )

    class Meta:
        verbose_name = '商品类别3'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Type4(models.Model):
    '''
    四级类目
    '''
    parent = models.ForeignKey(
        Type3,
        verbose_name='父级类别',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=10,
        default='',
        verbose_name='类目名'
    )
    add_time = models.DateTimeField(
        default=datetime.now,
        verbose_name='添加时间'
    )

    class Meta:
        verbose_name = '商品类别4'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
