from django.contrib import admin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "is_staff", "is_active",]
    ordering = ("email",)
    search_fields = ("email",)
    fieldsets = ((None, {
        "fields": ("email", "password",)
    }),)
    add_fieldsets = ((None, {
        "classes": ("wide",),
        "fields": ("email", "password1", "password2", "is_staff", "is_active",)
    }),)

admin.site.register(CustomUser, CustomUserAdmin)