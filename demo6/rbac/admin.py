from django.contrib import admin
from .models import User, Permission, Role
# Register your models here.

admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(User)

