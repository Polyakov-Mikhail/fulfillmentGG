from django.contrib import admin
from cabinet.models import Product, Dashboard, Supply, ProductAccept, Marketplace, DeliveryPoint, Shipment, ProductShipment


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


@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name',)


@admin.register(DeliveryPoint)
class DeliveryPointAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('name', 'city', 'address', 'marketplace', 'is_active')


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('shipment_date', 'owner', 'delivery_point', 'quantity_cargo', 'status', 'comment')


@admin.register(ProductShipment)
class ProductShipmentAdmin(admin.ModelAdmin):
    exclude = ('id', )
    list_display = ('owner', 'product', 'quantity', 'shipment')