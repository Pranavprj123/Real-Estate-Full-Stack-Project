from django.contrib import admin
from .models import VisitRequest

@admin.register(VisitRequest)
class VisitRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'property__title')
