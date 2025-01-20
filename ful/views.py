from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from ful.models import Start, FAQ, Services, CategoryFAQ, Warehouses, Employees

from services import get_models_from_cache


def index(request):
    context = {
        "title": "Home",
        "content": "Главная страница сайта"
    }
    return render(request, "ful/index.html", context)


class StartListView(ListView):
    model = Start

    def get_queryset(self):
        queryset = get_models_from_cache(Start)
        return queryset


class CategoryFAQListView(ListView):
    model = CategoryFAQ

    def faq_view(request):
        categories = CategoryFAQ.objects.all()
        context = {'categories': categories}
        return render(request, 'categoryfaq_list.html', context)

    def get_queryset(self):
        queryset = get_models_from_cache(CategoryFAQ)
        return queryset


class ServicesListView(ListView):
    model = Services

    def get_queryset(self):
        queryset = get_models_from_cache(Services)
        return queryset


class WarehousesListView(ListView):
    model = Warehouses

    def get_queryset(self):
        queryset = get_models_from_cache(Warehouses)
        return queryset


class WarehousesDetailView(DetailView):
    model = Warehouses

    def employees_view(request):
        warehouses = Warehouses.objects.all()
        context = {'warehouses': warehouses}
        return render(request, 'warehouses_detail.html', context)


class EmployeesListView(ListView):
    model = Employees

    def employees_view(request):
        warehouses = Warehouses.objects.all()
        context = {'warehouses': warehouses}
        return render(request, 'employees_list.html', context)