from django.contrib import admin
from .models import Customer, Consumption


class ConsumptionInline(admin.TabularInline):
    model = Consumption


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'number']
    list_filter = ['name', 'address', 'number']
    list_display_links = ['name', 'address', 'number']
    inlines = [ConsumptionInline]
    list_per_page = 15


@admin.register(Consumption)
class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ['cost', 'consumption', 'customer', 'rate', 'first', 'second']
    list_filter = ['cost', 'consumption', 'customer', 'rate', 'first', 'second']
    list_display_links = ['cost', 'consumption', 'customer', 'rate', 'first', 'second']
    list_per_page = 15
