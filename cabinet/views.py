from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.db.models import Sum

from cabinet.forms import ProductForm, SupplyForm
from cabinet.models import Product, Dashboard, Supply, ProductAccept
from users.models import User



class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Product.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Product.objects.none()


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


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('cabinet:product')



class DashboardListView(ListView):
    model = Dashboard

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        context['product_count'] = Product.objects.filter(is_active=True,owner=current_user).count()
        context['product_total_quantity'] = Product.objects.filter(is_active=True,owner=current_user).aggregate(Sum('quantity'))['quantity__sum']
        return context


class SupplyListView(ListView):
    model = Supply

    def get_queryset(self):
        # Проверяем, аутентифицирован ли пользователь
        if self.request.user.is_authenticated:
            # Возвращаем только клиентов, принадлежащих текущему пользователю
            return Supply.objects.filter(owner=self.request.user)
        # Возвращаем пустой queryset для неаутентифицированных пользователей
        return Supply.objects.none()


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


class SupplyDetailView(DetailView):
    model = Supply

    def product_accept_view(request):
        supplys = Supply.objects.all()
        context = {'supplys': supplys}
        return render(request, 'supply_detail.html', context)


# class ProductAcceptListView(ListView):
#     model = ProductAccept
#
#     def product_accept_view(request):
#         supplys = Supply.objects.all()
#         context = {'supplys': supplys}
#         return render(request, 'supply_detail.html', context)

    # success_url = reverse_lazy('messaging:client_list')
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     client_item = self.get_object()
    #     context['title'] = client_item.first_name
    #     return context

# class ProductAcceptCreateView(CreateView, LoginRequiredMixin):
#     model = ProductAccept
#     form_class = ProductAcceptForm
#     success_url = reverse_lazy('cabinet:supply_create')
#
#     def form_valid(self, form):
#         product = form.save()
#         user = self.request.user
#         product.owner = user
#         product.save()
#
#         return super().form_valid(form)