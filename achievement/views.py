from django.shortcuts import render

# Create your views here.

def achivement(request):
    return render(request, 'achievement/achievement.html')
