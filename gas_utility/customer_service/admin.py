from django.contrib import admin
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'request_type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'request_type')
    search_fields = ('customer_name', 'email', 'phone')
