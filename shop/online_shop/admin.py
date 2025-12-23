from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel, Service

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'is_staff', 'is_active',)
    list_display_links = ('username', 'email',)
    list_filter = ('is_staff', 'is_active', 'date_joined',)
    search_fields = ('username', 'email', 'first_name',)
    list_editable = ('is_active',)

    fieldsets = UserAdmin.fieldsets + (
        ('Дополнительный информация', {'fields': ('avatar',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Дополнительная информация', {'fields': ('first_name', 'avatar')}),
    )

admin.site.register(UserModel, CustomUserAdmin)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    fields = ('name', 'description', 'image', 'is_active')


