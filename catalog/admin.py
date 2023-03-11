from django.contrib import admin
from .models import Category, Country, Product, Manufacturer


@admin.register(Category)
class CategryAdmin(admin.ModelAdmin):
    list_display = ('category_name', )
    search_fields = ('category_name',)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
    search_fields = ('cuntry_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'count', 'guaranty')
    search_fields = ('product_name',)
    list_editable = ('count', 'guaranty')
    list_filter = ('guaranty',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer_name', 'address', 'phone')
    search_fields = ('manufacturer_name', 'address', 'phone')
    list_editable = ('address', 'phone')