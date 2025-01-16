from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ful import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="start"),
    path("", include("ful.urls", namespace="ful")),
    path("lk/", include("cabinet.urls", namespace="cabinet")),
    path("users/", include("users.urls", namespace="users")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
