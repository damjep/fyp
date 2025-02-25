from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Dish, Category, DishType

class UserAdmin(BaseUserAdmin):
    # Fields to be displayed in the admin list view
    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('email', 'name')
    ordering = ('email',)

    # Fieldsets for organizing the edit form
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login',)}),
        ('Shifts', {'fields': ('shift_available',)}),  # Add your shift field here

    )

    # Fields to be displayed during user creation
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )

admin.site.register(User, UserAdmin)
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(DishType)