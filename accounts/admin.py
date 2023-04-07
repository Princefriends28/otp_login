from django.contrib import admin

from .models import Profile


# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number']
    list_display_links = ('user',)
    list_per_page = 25
