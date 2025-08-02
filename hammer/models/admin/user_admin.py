from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User=get_user_model()

@admin.register(User)
class UserAdmin(UserAdmin):
    UserAdmin.fieldsets+= (('Custom fields', {'fields': ('invite_code', 'used_invite_code','phone_number')}),)
    list_display = ('id','phone_number', 'invite_code', 'used_invite_code')