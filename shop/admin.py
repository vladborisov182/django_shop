from django.contrib import admin
from shop.models import Category, Manufacturer, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'price', 'discount', 'price_with_discount', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'discount', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
