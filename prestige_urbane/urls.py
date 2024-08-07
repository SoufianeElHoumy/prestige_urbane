"""
URL configuration for prestige_urbane project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='home'),  # Add this line
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('cart/list/', views.list, name='list'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
    path('ordertracking/', views.ordertracking, name='ordertracking'),
    path('admin/',admin.site.urls , name='admin'),  
    path('shop/', views.shop, name='shop'),
    path('category/<str:category>/', views.category, name='category'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('landingpage/', views.landingpage, name='landingpage'),
]