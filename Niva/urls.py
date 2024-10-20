"""
URL configuration for Niva project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(("base.urls", "base"), "base")),
    path("articles/", include("base.urls")),
] + static(settings.STATIC_URL)
