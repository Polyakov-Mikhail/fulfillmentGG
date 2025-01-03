from django.urls import path

from ful.apps import FulConfig
from ful.views import StartListView

app_name = FulConfig.name

urlpatterns = [
    path('', StartListView.as_view(), name='start'),
]