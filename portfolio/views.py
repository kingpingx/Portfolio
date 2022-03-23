from django.shortcuts import redirect, render, HttpResponse


def home(request):
    return render(request,'Portfolio.html')