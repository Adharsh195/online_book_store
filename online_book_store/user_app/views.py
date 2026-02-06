from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def Register_user(request):
    if request.method=="POST":
        username=request.POST['username']
        email = request.POST['email'] 
        password = request.POST['password'] 
        confirm_password = request.POST['confirm_password']  
        if password != confirm_password: 
           return render(request, 'register.html', {'error': 'Passwords do not match!'}) 
        if User.objects.filter(username=username).exists(): 
          return render(request, 'register.html', {'error': 'Username already taken!'})
        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        # return redirect(login_user)
    return render(request, 'register.html') 

@login_required(login_url='login_user')
def dashboard(request):
    return render(request,'dashboard.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('dashboard')
        else:
            messages.error(request, "Invalid username or password!")
            return render(request, 'login.html')

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('logout_user')


