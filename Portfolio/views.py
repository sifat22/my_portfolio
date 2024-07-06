from django.shortcuts import render
from app_about.models import Home,About,Skill


def home(request):
    back = Home.objects.get(name = "Toushif Ahmed")
    about = About.objects.get(phone = "01797475300")
    return render(request,"home.html",{
        "back" : back,
        "about":about
    })