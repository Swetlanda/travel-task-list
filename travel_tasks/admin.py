from django.contrib import admin
from .models import TravelTask  # Import the TravelTask model


# Custom admin interface for the TravelTask model
class TravelTaskAdmin(admin.ModelAdmin):
    # Fields shown in the list view
    list_display = ('user', 'destination', 'status', 'start_date', 'end_date', 'created_on', 'updated_on')
    # Fields searchable in the admin
    search_fields = ('user__username', 'destination')
    # Fields available as filters
    list_filter = ('user__username', 'destination', 'status', 'start_date', 'created_on', 'updated_on')
    # Default ordering by user and start date
    ordering = ('user__username', 'start_date',)

# Register TravelTask with the custom admin interface
admin.site.register(TravelTask, TravelTaskAdmin)