from django.contrib import admin
from cabinet.models import Product, Dashboard, Supply, ProductAccept


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    exclude = ('id', )


@admin.register(ProductAccept)
class ProductAcceptAdmin(admin.ModelAdmin):
    exclude = ('id', )