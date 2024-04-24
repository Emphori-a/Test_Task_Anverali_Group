from django.contrib import admin

from .models import Order

admin.site.empty_value_display = 'Не задано'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'created_at', 'customer', 'executor')
    list_display_links = ('name',)
    list_per_page = 10
    list_filter = (
        'created_at',
        'customer',
        'executor',
    )
