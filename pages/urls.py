from django.urls import path
from . import views
from .views import login

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('ordertracking/', views.ordertracking, name='ordertracking'),
    path('shop/', views.shop, name='shop'),
    path('list/', views.cart, name='cart'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('register/', views.register, name='register'),
    path('landingpage/', views.landingpage, name='landingpage'),
    
]