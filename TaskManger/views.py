from django.shortcuts import render

def show_home_view(request):
    return render(request, 'home.html')