from django.contrib import admin

# Register your models here.
from .models import User, Item

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = list_display
    list_filter = list_display