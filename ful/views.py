from django.shortcuts import render

from django.views.generic import ListView
from ful.models import Start


class StartListView(ListView):
    model = Start