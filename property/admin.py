from django.contrib import admin

from .models import Flat, Complaint


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address',]
    readonly_fields = ['created_at',]
    list_display = ['address', 'price', 'new_building', 'construction_year',
                    'town']
    list_editable = ['new_building',]
    list_filter = ['new_building', 'rooms_number', 'has_balcony', 'active',
                   'floor']
    raw_id_fields = ['liked']


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['flat', 'user']
    raw_id_fields = ['flat', 'user']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
