from django.contrib import admin
from django.urls import path
from routing.apps.api import views


urlpatterns = [
    path('routing', views.routing_view),
]