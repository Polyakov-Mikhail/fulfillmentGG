from django.urls import path

from ful.apps import FulConfig
from ful.views import ServicesListView, CategoryFAQListView, WarehousesListView, WarehousesDetailView

app_name = FulConfig.name

urlpatterns = [
    path("services/", ServicesListView.as_view(), name="services"),
    path("faq/", CategoryFAQListView.as_view(), name="faq"),
    path("warehouses/", WarehousesListView.as_view(), name="warehouses"),
    path("warehouses/<slug:slug>/", WarehousesDetailView.as_view(), name="warehouses_detail"),
]
