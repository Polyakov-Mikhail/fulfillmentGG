from django.urls import path

from cabinet.apps import CabinetConfig
from cabinet.views import ProductListView, ProductCreateView, ProductDeleteView, ProductUpdateView, DashboardListView

app_name = CabinetConfig.name

urlpatterns = [
    path("", DashboardListView.as_view(), name="home"),
    path("product/", ProductListView.as_view(), name="product"),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),

]
