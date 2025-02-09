from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnedFlatsInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner', 'flat']


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['owner', 'town', 'address',]
    readonly_fields = ['created_at',]
    list_display = ['address', 'price', 'new_building', 'construction_year',
                    'town']
    list_editable = ['new_building',]
    list_filter = ['new_building', 'rooms_number', 'has_balcony', 'active',
                   'floor']
    raw_id_fields = ['liked_by']
    inlines = [OwnedFlatsInline]


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = ['flat', 'user']
    raw_id_fields = ['flat', 'user']


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'phonenumber',]
    raw_id_fields = ['flats',]
