from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from ful.models import Start, FAQ, Services, CategoryFAQ, Warehouses


def index(request):
    context = {
        "title": "Home",
        "content": "Главная страница сайта"
    }
    return render(request, "ful/index.html", context)


class StartListView(ListView):
    model = Start


class CategoryFAQListView(ListView):
    model = CategoryFAQ

    def faq_view(request):
        categories = CategoryFAQ.objects.all()
        context = {'categories': categories}
        return render(request, 'categoryfaq_list.html', context)


class ServicesListView(ListView):
    model = Services


class WarehousesListView(ListView):
    model = Warehouses



class WarehousesDetailView(DetailView):
    model = Warehouses

    def employees_view(request):
        warehouses = Warehouses.objects.all()
        context = {'warehouses': warehouses}
        return render(request, 'warehouses_detail.html', context)