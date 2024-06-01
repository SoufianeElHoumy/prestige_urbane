from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.index, name='Home'),
    path('about/', views.about, name='About'),
    path('services/', views.services, name='Services'),
    path('contact/', views.contact, name='Contact'),
    path('pricing/', views.pricing, name='Pricing'),
]