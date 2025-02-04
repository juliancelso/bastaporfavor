from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role_id', 'dni', 'phone', 'department')
    search_fields = ('username', 'email', 'dni', 'phone')