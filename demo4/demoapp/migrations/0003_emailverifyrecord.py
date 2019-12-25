# Generated by Django 3.0 on 2019-12-18 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='激活码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
    ]
