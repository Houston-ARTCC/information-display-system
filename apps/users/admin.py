from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from ..users.models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    model = User
    list_display = ('cid', 'email', 'first_name', 'last_name')
    search_fields = list_display
    list_filter = list_display
    ordering = ('cid',)
    fieldsets = (
        ('Personal Information', {'fields': ('cid', 'first_name', 'last_name', 'email', 'password')}),
        ('Facilities', {'fields': ('facilities',)}),
        ('Permissions', {'fields': ('is_superuser', 'user_permissions')}),
    )
