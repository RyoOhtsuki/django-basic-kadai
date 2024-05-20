from django.contrib import admin
from crud.models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    search_fields = ('name', )

admin.site.register(Product, ProductAdmin)
