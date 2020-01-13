from rbac.models import User, Permission, Role

def initial_permission(user, request):
    # 查询角色
    ret = user.role.all()
    permission_list = []
    for item in ret:
        rep = Permission.objects.filter(role__title=item)
        for item2 in rep:
            permission_list.append(item2.url)
    request.session["perimission_list"] = permission_list