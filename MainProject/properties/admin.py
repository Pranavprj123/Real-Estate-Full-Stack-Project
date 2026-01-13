from django.contrib import admin
from .models import Property

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'price', 'bhk', 'created_at')
    search_fields = ('title', 'city')
    list_filter = ('city', 'bhk')
    ordering = ('-created_at',)