from django.urls import path

from cabinet.apps import CabinetConfig
from cabinet.views import ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView, DashboardListView, \
    SupplyListView, SupplyCreateView, SupplyUpdateView, SupplyDetailView, ProductAcceptCreateView, \
    ProductAcceptUpdateView, ShipmentListView, ShipmentCreateView, ShipmentDetailView, ShipmentUpdateView, \
    ProductShipmentCreateView, ProductShipmentUpdateView, ProductAcceptDeleteView, ProductShipmentDeleteView, \
    CompanyListView

app_name = CabinetConfig.name

urlpatterns = [
    path("", DashboardListView.as_view(), name="home"),
    path("product/", ProductListView.as_view(), name="product"),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

    path("supply/", SupplyListView.as_view(), name="supply"),
    path('supply/<int:pk>/', SupplyDetailView.as_view(), name='supply_detail'),
    path('supply/create/', SupplyCreateView.as_view(), name='supply_create'),
    path('supply/update/<int:pk>/', SupplyUpdateView.as_view(), name='supply_update'),

    path('product_accept/create/', ProductAcceptCreateView.as_view(), name='product_accept_create'),
    path('product_accept/<int:pk>/', ProductAcceptUpdateView.as_view(), name='product_accept_update'),
    path('product_accept/delete/<int:pk>/', ProductAcceptDeleteView.as_view(), name='product_accept_delete'),

    path("shipment/", ShipmentListView.as_view(), name="shipment"),
    path('shipment/<int:pk>/', ShipmentDetailView.as_view(), name='shipment_detail'),
    path('shipment/create/', ShipmentCreateView.as_view(), name='shipment_create'),
    path('shipment/update/<int:pk>/', ShipmentUpdateView.as_view(), name='shipment_update'),

    path('product_shipment/create/', ProductShipmentCreateView.as_view(), name='product_shipment_create'),
    path('product_shipment/<int:pk>/', ProductShipmentUpdateView.as_view(), name='product_shipment_update'),
    path('product_shipment/delete/<int:pk>/', ProductShipmentDeleteView.as_view(), name='product_shipment_delete'),

    path("company/", CompanyListView.as_view(), name="company"),

]
