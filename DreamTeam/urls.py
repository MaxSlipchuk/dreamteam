"""
URL configuration for DreamTeam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from achievement import views as ach_views
from education import views as ed_views
from galary import views as gal_views
from hobby import views as hob_views
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("achievement/", ach_views.achivement),
    path("education/", ed_views.education),
    path("galary/", gal_views.galary),
    path("hobby/", hob_views.hobby),
    path("main/", main_views.main)
]
