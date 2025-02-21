from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.utils import IntegrityError




def render_registr(request):
    name = False
    password_confirmation = False
    

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password_confirmation = request.POST.get("password_confirmation")
        if password == password_confirmation:
            try:
                User.objects.create_user(username=username, password=password)

                return redirect("login")
            except IntegrityError:
                name = True
        else:
            password_confirmation = True
    return render(
        request=request,
        template_name="registration.html",
        context={
            "name": name,
            "password_confirmation": password_confirmation
        }
    )




def render_login(request):
    user = True
    next = request.GET.get('next', '/home_after')

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect(next)  
        
        else:
            user = None

    return render(request, "login.html", {"user": user})



def logout_user(request):
    logout(request)
    return redirect('home')
    