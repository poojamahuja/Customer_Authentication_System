from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customer


class CustomUserAdmin(UserAdmin):
    list_display = (
        'username','gender','is_customer',
    )

admin.site.register(Customer)
