from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display= ("username","first_name", "last_name","email","last_login","is_active",)
    list_display_links = ("username","first_name")
    readonly_fields = ("last_login","date_joined")
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        ("Personal info", {"fields": ("first_name", "last_name","username", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superadmin",
                ),
            },
        ),
    )
admin.site.register(Account,AccountAdmin)