from django.contrib import admin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import ngettext

from accounts.forms import UserAdminChangeForm, UserRegistrationForm

User = get_user_model()

admin.site.site_header = "Login Logic Admin"
admin.site.site_title = "Login Logic Admin Area"
admin.site.index_title = "Welcome to the Login Logic Admin Area"

admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserRegistrationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('first_name', 'last_name', 'email', 'username', 'country')
    search_fields = ('first_name', 'last_name', 'email', 'username',)
    list_filter = ('is_active', 'is_archived', 'updated', 'created')
    actions = ['make_active', 'make_inactive']

    fieldsets = (
        (None, {'fields': ('password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'username', 'country')}),
        ('Permissions', {'fields': ('is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'username', 'country', 'password1', 'password2')}
         ),
    )
    ordering = ['email']
    filter_horizontal = ()

    def make_active(self, request, queryset):
        updated = queryset.update(is_active=True, is_archived=False, is_approved=True)
        self.message_user(request, ngettext(
            '%d User has successfully been marked as active.',
            '%d Users have been successfully marked as active.',
            updated,
        ) % updated, messages.SUCCESS)

    make_active.short_description = "Approve User"

    def make_inactive(self, request, queryset):
        updated = queryset.update(is_archived=True, is_active=False)
        self.message_user(request, ngettext(
            '%d User has been archived successfully.',
            '%d Users have been archived successfully.',
            updated,
        ) % updated, messages.INFO)

    make_inactive.short_description = "Archive User"

    def has_delete_permission(self, request, obj=None):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request, obj=None):
        return True
