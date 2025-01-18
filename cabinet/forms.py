from django.forms import ModelForm

from cabinet.models import Product, Supply


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ("owner", "is_active", "created_at", "updated_at")


class SupplyForm(ModelForm):
    class Meta:
        model = Supply
        exclude = ("owner", "status",)