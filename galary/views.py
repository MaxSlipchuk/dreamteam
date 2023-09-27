from django.shortcuts import render

# Create your views here.

def galary(request):
    return render(request, 'galary/galary.html')