from django.contrib import admin
from cabinet.models import Product, Dashboard, Supply, ProductAccept


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name', 'article', 'barcode', 'quantity', 'owner', 'is_active',)


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('delivery_date', 'owner', 'quantity_cargo', 'status',)


@admin.register(ProductAccept)
class ProductAcceptAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('product', 'quantity', 'supply', 'owner',)