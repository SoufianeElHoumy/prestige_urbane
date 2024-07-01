from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('account/', views.account, name='account'),
    path('ordertracking/', views.ordertracking, name='ordertracking'),
]