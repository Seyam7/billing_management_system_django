from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from buyer.models import BuyerTable

# Create your views here.
def user_login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
            #print('name:'+username)
        else:
            #print('user not found')
            messages.warning(request, 'Invalid username or password.')
    return render(request,'./auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

def user_register(request):
    if request.method=='POST':
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        #contact,gender,address are not included
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email is already exists.')
            return redirect('register')
        elif User.objects.filter(username=username).exists():
            messages.warning(request, 'Username is already exists.')
            return redirect('register')
        else:
            user = User(first_name=firstname,last_name=lastname,
            username=username,password=password,email=email)
            user.set_password(password)
            user.save()

            data=BuyerTable()
            data.user=user
            data.contact=contact
            data.gender=gender
            data.address=address
            #data.email=email
            data.save()
            messages.success(request, 'New user has been registered successfully.')
            return redirect('/')
    return render(request,'./auth/register.html')
