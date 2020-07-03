from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('another', views.another, name='how to'),
    path('why', views.why, name='why'),
    path('donate', views.donate, name='donate'),
    path('scammed', views.scammed, name='joke'),
    path('create', views.create, name='create')
]
