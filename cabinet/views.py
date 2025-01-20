from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.signals import post_save
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.db.models import Sum
from django.dispatch import receiver
from django.contrib import messages

from cabinet.forms import ProductForm, SupplyForm, ProductAcceptForm, ShipmentForm, ProductShipmentForm
from cabinet.models import Product, Dashboard, Supply, ProductAccept, Shipment, ProductShipment, Company
from users.models import User


class DashboardListView(ListView):
    model = Dashboard

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Dashboard.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Dashboard.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['product_count'] = Product.objects.filter(is_active=True,owner=current_user).count()
        context['product_total_quantity'] = Product.objects.filter(is_active=True, owner=current_user).aggregate(Sum('quantity'))['quantity__sum']
        context['supply_total_quantity'] = Supply.objects.filter(owner=current_user,).count()
        context['shipment_total_quantity'] = Shipment.objects.filter(owner=current_user,).count()
        return context


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Product.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Product.objects.none()


    @receiver(post_save, sender=Supply)
    def update_product_quantity(sender, instance, **kwargs):
        if instance.status == Supply.StatusSupply.ACCEPTED:
            product_accepts = ProductAccept.objects.filter(supply=instance)
            for product_accept in product_accepts:
                product = product_accept.product
                if product:
                    product.quantity += product_accept.quantity
                    product.save()


    @receiver(post_save, sender=Shipment)
    def update_product_quantity_shipment(sender, instance, **kwargs):
        if instance.status == Shipment.StatusShipment.WAY:
            products_shipment = ProductShipment.objects.filter(shipment=instance)
            for product_shipment in products_shipment:
                product = product_shipment.product
                if product:
                    product.quantity -= product_shipment.quantity
                    product.save()


class ProductCreateView(CreateView, LoginRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('cabinet:product')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('cabinet:product')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Product.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Product.objects.none()


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('cabinet:product')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Product.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Product.objects.none()


class SupplyListView(ListView):
    model = Supply

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Supply.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Supply.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['product_accept_count'] = Supply.objects.filter(owner=current_user,).count()
        return context


class SupplyCreateView(CreateView, LoginRequiredMixin):
    model = Supply
    form_class = SupplyForm
    success_url = reverse_lazy('cabinet:supply')

    def form_valid(self, form):
        supply = form.save()
        user = self.request.user
        supply.owner = user
        supply.save()

        return super().form_valid(form)


class SupplyUpdateView(UpdateView):
    model = Supply
    form_class = SupplyForm
    success_url = reverse_lazy('cabinet:supply')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Supply.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Supply.objects.none()


class SupplyDetailView(DetailView):
    model = Supply

    def supplys_view(request):
        supplys = Supply.objects.all()
        context = {'supplys': supplys}
        return render(request, 'supply_detail.html', context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получаем объекты Product через ProductAccept
        context['products'] = Product.objects.filter(product_supply__supply=self.object)
        return context

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Supply.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Supply.objects.none()


class ProductAcceptCreateView(CreateView, LoginRequiredMixin):
    model = ProductAccept
    form_class = ProductAcceptForm
    success_url = reverse_lazy('cabinet:product_accept_create')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        messages.success(self.request, 'Товар добавлен')

        return super().form_valid(form)


class ProductAcceptUpdateView(UpdateView):
    model = ProductAccept
    form_class = ProductAcceptForm
    success_url = reverse_lazy('cabinet:product_accept_create')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return ProductAccept.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return ProductAccept.objects.none()


class ProductAcceptDeleteView(DeleteView):
    model = ProductAccept
    success_url = reverse_lazy('cabinet:supply')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return ProductAccept.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return ProductAccept.objects.none()


class ShipmentListView(ListView):
    model = Shipment

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Shipment.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Shipment.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['product_shipment_count'] = Shipment.objects.filter(owner=current_user,).count()
        return context


class ShipmentCreateView(CreateView, LoginRequiredMixin):
    model = Shipment
    form_class = ShipmentForm
    success_url = reverse_lazy('cabinet:shipment')

    def form_valid(self, form):
        shipment = form.save()
        user = self.request.user
        shipment.owner = user
        shipment.save()

        return super().form_valid(form)


class ShipmentUpdateView(UpdateView):
    model = Shipment
    form_class = ShipmentForm
    success_url = reverse_lazy('cabinet:shipment')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Shipment.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Shipment.objects.none()


class ShipmentDetailView(DetailView):
    model = Shipment

    def shipments_view(request):
        shipments = Shipment.objects.all()
        context = {'shipments': shipments}
        return render(request, 'shipment_detail.html', context)


    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Shipment.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Shipment.objects.none()

class ProductShipmentCreateView(CreateView, LoginRequiredMixin):
    model = ProductShipment
    form_class = ProductShipmentForm
    success_url = reverse_lazy('cabinet:product_shipment_create')

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        messages.success(self.request, 'Товар добавлен')

        return super().form_valid(form)


class ProductShipmentUpdateView(UpdateView):
    model = ProductShipment
    form_class = ProductShipmentForm
    success_url = reverse_lazy('cabinet:product_shipment_create')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return ProductShipment.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return ProductShipment.objects.none()


class ProductShipmentDeleteView(DeleteView):
    model = ProductShipment
    success_url = reverse_lazy('cabinet:shipment')

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return ProductShipment.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return ProductShipment.objects.none()


class CompanyListView(ListView):
    model = Company

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Company.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Company.objects.none()