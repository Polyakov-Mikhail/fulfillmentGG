from django.forms import ModelForm

from cabinet.models import Product, Supply, ProductAccept, Shipment, ProductShipment


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("owner", "is_active", "created_at", "updated_at",)


class SupplyForm(ModelForm):
    class Meta:
        model = Supply
        exclude = ("owner", "status",)


class ProductAcceptForm(ModelForm):
    class Meta:
        model = ProductAccept
        exclude = ("owner",)


class ShipmentForm(ModelForm):
    class Meta:
        model = Shipment
        exclude = ("owner", "status", "quantity_cargo", )


class ProductShipmentForm(ModelForm):
    class Meta:
        model = ProductShipment
        exclude = ("owner",)