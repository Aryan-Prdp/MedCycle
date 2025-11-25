from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_medicine, name='add_medicine'),
    path('donate/<int:med_id>/', views.donate, name='donate'),
    path('ngo-map/', views.ngo_map, name='ngo_map'),
]



