from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about-us.html')

def blog(request):
    return render(request, 'pages/blog.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def contact(request):
    return render(request, 'pages/contact-us.html')

def login(request):
    return render(request, 'pages/login.html')

def account(request):
    return render(request, 'pages/my-account.html')

def ordertracking(request):
    return render(request, 'pages/order-tracking.html')

def register(request):
    return render(request, 'pages/register.html')

def shop(request):
    return render(request, 'pages/shop.html')

def thankyou(request):
    return render(request, 'pages/thankyou.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html')

def list(request):
    return render(request, 'pages/list.html')

def details(request):
    return render(request, 'pages/details.html')
