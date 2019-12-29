from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from improved_user.forms import UserCreationForm, UserChangeForm
from Accounts.models import User
from Organizations.models import Ability, Organization, Membership


class AbilityInline(admin.TabularInline):
    model = Ability
    extra = 0


class MembershipInline(admin.TabularInline):
    model = Membership
    extra = 0
    autocomplete_fields = ('user',)


class CustomUserAdmin(UserAdmin):
    """An admin panel for our custom user model, mimics Django's default."""
    def email_link(self, user):
        return format_html(f'<a href="mailto:{user.email}">{user.email}</a>')
    email_link.short_description = "E-Mail"
    email_link.admin_order_field = 'email'

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
    list_display = ('short_name', 'full_name', 'email_link', 'is_staff')
    search_fields = ('email', 'full_name', 'short_name')
    ordering = ('short_name',)
    list_filter = ('membership__orga', 'is_staff', 'is_superuser', 'is_active')
    inlines = (AbilityInline, MembershipInline)

admin.site.register(User, CustomUserAdmin)


class AbilityAdmin(admin.ModelAdmin):
    search_fields = ('kind', 'number', 'remark')
    date_hierarchy = 'expires'

admin.site.register(Ability, AbilityAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    inlines = (MembershipInline,)

admin.site.register(Organization, OrganizationAdmin)
