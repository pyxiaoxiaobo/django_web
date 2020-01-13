from django.shortcuts import render, HttpResponse, redirect
from rbac.models import User, Permission
from rbac.service.permission import initial_permission
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('usernmae')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=username, pwd=pwd).first()
        if user:
            request.session["user_id"] = user.pk
            re = user.role.all().values('permisssion__url')
            permission_list = []
            for item in re:
                permission_list.append(item['permission__url'])
            request.session["permission_list"] = permission_list
            return HttpResponse('登录成功')
        return render(request, 'login.html')


def login2(request):
    if request.method == "POST":
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=username, pwd=pwd).first()
        if user:
            request.session['user_id'] = user.pk
            initial_permission(user, request)
            return HttpResponse('登录成功')
    return render(request, 'login.html')


import re

def user(request):
    # 获取session键值, 如果不存在不报错， 返回None
    permission_list = request.session.get('permission_list', [])
    print(permission_list)
    path = request.path_info
    flag = False
    for permission in permission_list:
        permission = "^%s$"%permission
        ret = re.match(permission, path)
        if ret:
            flag=True
            break
    if not flag:
        return HttpResponse('无法访问权限')
    return HttpResponse('查看用户')

# def userinfo(request):
#     # 首先进行身份验证
#     pk = request.session.get('user_id')
#     if not pk:
#         return redirect('/login/')
#     user = Userinfo.objects.filter(id=pk).first()
#     p_list = []
#     p_queryset = user.permission.all()
#     for p in p_queryset:
#         p_list.append(p.url)
#     p_list = list(set(p_list))
#     c = request.path_info
#     if c in p_list:
#         u_queryset = Userinfo.objects.all()
#         return render(request, "userinfo.html", {"u_queryset": u_queryset})
#     else:
#         return HttpResponse('没有权限')