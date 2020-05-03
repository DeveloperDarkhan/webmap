from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin



# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'username', 'is_staff', 'is_active', 
    'age', 'date_joined',)
    list_filter = ('email', 'username', 'is_staff', 'is_active', 
    'age', 'date_joined',)

admin.site.register(CustomUser, CustomUserAdmin)