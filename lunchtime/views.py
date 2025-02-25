from django.shortcuts import render

def home(request):
    return render(request, 'lunchtime/home.html')

def dramas(request):
    return render(request, 'lunchtime/dramas.html')