from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Con la siguiente importacion se permite traducir la APP,
# segun el idiona definido en DJANGO.
from django.utils.translation import gettext_lazy as _

from user.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'username']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('username',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ['last_login', 'date_joined']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'username',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )
