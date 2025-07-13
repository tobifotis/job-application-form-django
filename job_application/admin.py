from django.contrib import admin

# import submission data from database
from .models import Form


class FormAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Form model.
    Controls how job application submissions are displayed and managed in the admin panel.
    """
    list_display = ("first_name", "last_name", "email")  # Fields to show in the list view
    search_fields = ("first_name", "last_name", "email")  # Enable search on these fields
    list_filter = ("date", "occupation")  # Add filter options in the sidebar
    ordering = ("first_name",)  # Default ordering by first name
    readonly_fields = ("email", "occupation",)  # Make these fields read-only in the detail view


# Register the Form model with the custom admin configuration
admin.site.register(Form, FormAdmin)
