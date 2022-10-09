from django.contrib import admin
from creativescienceapp.models import Role,User,Token

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('id','complete_name','username','email','password','profile_image','verified','role_id')
    readonly_fields= ('id',)
class RoleAdmin(admin.ModelAdmin):
    list_display=('id','name')
    
class TokenAdmin(admin.ModelAdmin):
    list_display=('user_id','token')
admin.site.register(Role,RoleAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(Token,TokenAdmin)