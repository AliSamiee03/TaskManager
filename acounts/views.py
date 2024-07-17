from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_view(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email= email, password= password)
        if user is not None :
            login(request, user)
            messages.info(request, "success", extra_tags='success')
            return redirect('Home')
        else:
            messages.info(request, "error", extra_tags='error')
            return redirect('login')
    
    else :
        return render(request, 'accounts/login.html')
    
def logout_view(request):

    logout(request)
    messages.info(request, 'logout', extra_tags='logout')
    return redirect('Home')