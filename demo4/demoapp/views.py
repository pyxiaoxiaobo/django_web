from django.shortcuts import render, HttpResponse
import json
import re
import datetime
import random
from demo4.settings import APIKEY
from .models import Code, UserDemo4, EmailVerifyRecord
from utils.yuanpian import YunPian
from utils.email_send import send_register_email
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# Create your views here.

class SendActiveCodeView(APIView):
    '''
    发送激活连接类
    '''
    def get(self, request):
        email = request.GET.get('email')
        if email:
            send_register_email(email)
            msg = '激活连接已发送, 请前往邮箱完成激活'
            result = {"status": 200,
                      "data": {msg: msg}}
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json, charset=utf-8")
        else:
            msg = '未收到邮箱'
            result = {
                "sttus": 404,
                "data": {'msg': msg}
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json, charset=utf-8")


class ActiveView(APIView):
    '''
    激活认证用户类
    '''
    def get(self, request, code):
        item = EmailVerifyRecord.objects.filter(code=code).last()
        if item:
            email = item.email
            user = UserDemo4.objects.filter(email=email).first()
            user.is_auther = True
            user.save()
            return HttpResponse('success')
        else:
            return HttpResponse('failed')



class RegisterView(APIView):
    '''
    注册类
    '''
    def get(self, request):
        username = request.GET.gt('username')
        pwd = request.GET.get('pwd')
        phone = request.GET.get('phone')
        email = request.GET.get('email')
        code = request.GET.get('code')
        if username:
            pass
        else:
            msg = '用户名不能为空'
            result = {
                "status": "404",
                "data": {"msg": msg}
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json, charset=utf-8")
        if pwd:
            pass
        else:
            msg = '密码不能为空'
            result = {
                "status": "404",
                "data": {"msg": msg}
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json, charset=utf-8")
        if email:
            pass
        else:
            msg = '邮箱不能为空'
            result = {
                "status": "404",
                "data": {"msg": msg}
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json, charset=utf-8")
        if code:
            pass
        else:
            msg = '验证码不能为空'
            result = {
                "status": "404",
                "data": {"msg": msg}
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json, charset=utf-8")
        code1 = Code.objects.filter(phone=phone).last()
        if code==code1:
            end_time = code1.end_time
            end_time = end_time.replace(tzinfo=None)
            if end_time > datetime.datetime.now():
                user = UserDemo4()
                user.username = username
                user.password = pwd
                user.phone = phone
                user.email = email
                user.save()
                msg = '注册成功'
                result = {
                    "status": "200",
                    "data": {
                        'msg': msg
                    }
                }
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="appliation/json, charset=utf-8")
            else:
                msg = "验证码已过期"
                result = {
                    "status": "200",
                    "data": {"msg": msg}
                }
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json,charset=utf-8")
        else:
            msg = "验证码错误"
            result = {
                "status": "403",
                "data": {"msg": msg}
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json,charset=utf-8")

class SendCodeView(APIView):
    '''
    获取手机验证码
    '''
    def get(self, request):
        phone  = request.GET.get('phone')
        if phone:
            # 验证是否为有效手机号
            mobile_pat = re.compile('^(13\d|14[5|7]|15\d|166|17\d|18\d)\d{8}$')
            res = re.search(mobile_pat, phone)
            if res:
                had_register = UserDemo4.objects.filter(phone=phone)
                if had_register:
                    msg = "手机号已被注册"
                    result = {
                        "status": "402",
                        "data": {'msg': msg}
                    }
                    return  HttpResponse(json.dumps(result, ensure_ascii=False),
                                         content_type="application/json",
                                         charset="utf-8")
                else:
                    had_send = Code.objects.filter(phone=phone).last()
                    if had_send:
                        if had_send.add_time.replace(tzinfo=None) > (
                            datetime.datetime.now() - datetime.timedelta(minutes=1)
                        ):
                            msg = "距离上次发送验证码不足1分钟"
                            result = {"status": "403", "data": {'msg': msg}}
                            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                                content_type="application/json, charset=utf-8")
                        else:
                            code = Code()
                            code.phone = phone
                            c = random.randint(1000, 9999)
                            code.code = str(c)
                            code.end_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
                            code.save()
                            code = Code.objects.filter(phone=phone).last().code
                            yunpian = YunPian(APIKEY)
                            sms_staus = yunpian.send_sms(code=code, mobile=phone)
                            msg = sms_staus
                            return HttpResponse(msg)
                    else:
                        code = Code()
                        code.phone = phone
                        c= random.randint(1000, 9999)
                        code.code = str(c)
                        code.end_time = datetime.datetime.now() + datetime.timedelta(minutes=20)
                        code.save()
                        code = Code.objects.filter(phone=phone).last().code
                        yunpian = YunPian(APIKEY)
                        sms_status = yunpian.send_sms(code=code, mobile=phone)
                        msg = sms_status
                        return HttpResponse(msg)
            else:
                msg = '手机号不合法!'
                result = {
                    "status": "403",
                    "data": {"msg": msg}
                }
                return HttpResponse(json.dumps(result, ensure_ascii=False),
                                    content_type="application/json, charset=utf-8")
        else:
            msg = "手机号为空"
            result = {
                "status": "404",
                "data": {"msg": msg}
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False),
                                content_type="application/json", charset='utf-8')