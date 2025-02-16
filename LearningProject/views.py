from django.http import HttpResponse
from django.shortcuts import render

def aboutUs(request):
    return render(request,"index.html")

def aboutUs1(request,abs1):
    return HttpResponse("Integer Based Dynamic URL creation")

def aboutUs2(request,abs2):
    return HttpResponse("String Based Dynamic URL creation")

def aboutUs3(request,abs3):
    return HttpResponse("slug Based Dynamic URL creation")

def aboutUs4(request):
    return HttpResponse("Combined Dynamic URL creation")
