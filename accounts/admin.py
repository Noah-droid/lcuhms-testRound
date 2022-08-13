from django.contrib import admin
from .models import CustomUser
from .form import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin




admin.site.site_header = "HMS Admin"
admin.site.site_title = "HMS Admin Area"
admin.site.index_title = "Welcome to the LEAD CITY HMS Admin Area"

# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Info',
            {
                'fields':(
                    'DOB',
                    'phone_number',
                    'Gender'
                )
            }
        )
    )


admin.site.register(CustomUser, CustomUserAdmin)