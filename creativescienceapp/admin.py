from django.contrib import admin
from creativescienceapp.models import Role,User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=("id","complete_name","username","email","password","verified","role_id")

class RoleAdmin(admin.ModelAdmin):
    list_display=("id","name")
admin.site.register(Role,RoleAdmin)
admin.site.register(User,UserAdmin)
