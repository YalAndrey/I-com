from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.comics, name='comics')
] + static(settings.STATIC_URL,  document_root=settings.STATIC_ROOT)
