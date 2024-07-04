from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from .models import Post 
from django.contrib.auth.models import User
from django.contrib import messages
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

def account(request):
    return render(request, 'pages/my-account.html')

def ordertracking(request):
    return render(request, 'pages/order-tracking.html')

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'pages/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST['name']
        password = request.POST['password']
        if  User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'You are now registered and can log in')
            return redirect('login')
    else:
         return render(request, 'pages/register.html')

 # make sure to import your Post model

def shop(request):
    posts = Post.objects.all()  # fetch all posts
    return render(request, 'pages/shop.html', {'posts': posts})

def thankyou(request):
    return render(request, 'pages/thankyou.html')

def list(request):
    return render(request, 'pages/cart/list.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html')

def cart(request):
    return render(request, 'pages/list.html')

def details(request):
    return render(request, 'pages/details.html')


def category(request , category):
    referrer = category 
    print("-----> here i am " ,referrer )
    # Determine the context variable based on the referrer
    if 'jeans' in referrer:
        posts = Post.objects.filter(item_name__startswith='jeans')
        context = {'category': 'jeans' , 'posts' : posts}
    elif 'jackets' in referrer:
        posts = Post.objects.filter(item_name__startswith='jacket')
        context = {'category': 'jacket',  'posts' : posts}
    else:
        posts = Post.objects.filter(item_name__startswith='T-Shirt')
        context = {'category': 'T-Shirts' , 'posts' : posts}
    return render(request, 'pages/category.html', context)
    
