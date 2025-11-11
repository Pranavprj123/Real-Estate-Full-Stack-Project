from django.contrib import admin
from .models import AgentProfile

@admin.register(AgentProfile)
class AgentProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_agent_verified')
    list_editable = ('is_agent_verified',)

