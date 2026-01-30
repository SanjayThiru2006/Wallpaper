from django.shortcuts import render,redirect
import random
from .models import *
from django.contrib.auth import authenticate
from django.contrib import messages

def login(request):
    if 'phone_number' in request.session:
        return redirect('/products/')

    return render(request,'login.html')


def send_otp(request):
    if 'phone_number' in request.session:
        return redirect('/products/')

    if request.method=="POST":
        phone = request.POST.get('phone')
        num = random.randint(100000, 999999)
        print(phone,num)
        if User.objects.filter(phone_number=phone).exists():
            OTP.objects.filter(phone_number=phone).delete()
            OTP.objects.create(phone_number=phone , otp=num)
            return render(request,'verify_otp.html' , {'phone' : phone} )
        else:
            messages.info(request , "User not found. Please Register")
            return redirect('/')

def verify_otp(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        entered_otp = request.POST.get('otp')
        row = OTP.objects.get(phone_number=phone)
        default_otp = row.otp
        print(phone , entered_otp , default_otp)
        if entered_otp==default_otp:
            request.session['phone_number']=phone
            return redirect('/products/')

def products(request):
    if 'phone_number' not in request.session:
        return redirect('/')
    category = Category.objects.all().order_by('name')
    product = Product.objects.all().order_by('name')
    return render(request,'products.html' ,{'category' : category , 'product' : product})

def logout_view(request):
    request.session.flush()
    return redirect('/')

def cart(request):
    return render(request , 'cart.html')