from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from improved_user.forms import UserCreationForm, UserChangeForm
from Organizations.models import User


class CustomUserAdmin(UserAdmin):
    """An admin panel for our custom user model, mimics Django's default."""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('full_name', 'short_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'short_name', 'password1', 'password2'),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('email', 'full_name', 'short_name', 'is_staff')
    search_fields = ('email', 'full_name', 'short_name')
    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)
