from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('another.html', views.another)
]
