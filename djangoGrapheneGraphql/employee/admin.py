from django.contrib import admin
from .models import Occupation


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'position_name',
                    'hire_date', 'fire_date', 'salary',
                    'fraction', 'base', 'advance', 'by_hours')
    list_display_links = ('name', )
    list_editable = ('by_hours',)
