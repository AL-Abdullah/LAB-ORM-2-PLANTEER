from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_plant, name='add_plant'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('plant/<int:pk>/update/', views.plant_update, name='plant_update'),
    path('plant/<int:pk>/delete/', views.plant_delete, name='plant_delete'),
    path('all-plants/', views.all_plants, name='all_plants'),
    path('contact_us/', views.contact_us, name='contact_us'),
]