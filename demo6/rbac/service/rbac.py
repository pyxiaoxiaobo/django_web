import re
from django.shortcuts import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class ValidPermission(MiddlewareMixin):
    '''权限验证中间件类'''

    def process_request(self, request):
        # 获取session键值， 如果不存在， 不报错， 返回[]
        permission_list = request.session.get('permission_list', [])
        print(permission_list)
        path = request.path_info
        valid_url_list = ["/login/", '/register/', '/admin/.*']
        for valid in valid_url_list:
            ret = re.match(valid, path)
            if ret:
                return None
        flag = False
        for permission in permission_list:
            permission = "^%s$" % permission
            ret = re.match(permission, path)
            if ret:
                flag = True
                break
            print(flag)
            if not flag:
                return HttpResponse('无访问权限')
            return None