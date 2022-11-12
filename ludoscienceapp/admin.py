from django.contrib import admin
from ludoscienceapp.models.role import Role
from ludoscienceapp.models.user import User
from ludoscienceapp.models.proyect import Proyect
from ludoscienceapp.models.badge import Badge
from ludoscienceapp.models.token import Token
from ludoscienceapp.models.check_in import CheckIn

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','complete_name','username','email','password','profile_image','verified','role_id')
    readonly_fields= ('id',)
class RoleAdmin(admin.ModelAdmin):
    list_display=('id','name')

class ProyectAdmin(admin.ModelAdmin):
    list_display=('id','name','description','image')
    
class TokenAdmin(admin.ModelAdmin):
    list_display=('user_id','token')

class BadgeAdmin(admin.ModelAdmin):
    list_display=('image','parent')

class AreaAdmin(admin.ModelAdmin):
    list_display=('lat','long')

class CheckInAdmin(admin.ModelAdmin):
    list_display=('user','proyect','latitude','longitude','datetime')

admin.site.register(Role,RoleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Token,TokenAdmin)
admin.site.register(Proyect,ProyectAdmin)
admin.site.register(Badge,BadgeAdmin)
admin.site.register(CheckIn,CheckInAdmin)