from django.contrib import admin
from .models import VisitRequest

@admin.register(VisitRequest)
class VisitRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'property', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'property__title')
    actions = ['approve_visits', 'reject_visits']

    @admin.action(description="Approve selected visit requests")
    def approve_visits(self, request, queryset):
        queryset.update(status='approved')

    @admin.action(description="Reject selected visit requests")
    def reject_visits(self, request, queryset):
        queryset.update(status='rejected')
