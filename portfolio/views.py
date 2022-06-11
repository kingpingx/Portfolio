from django.shortcuts import redirect, render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    if request.method=='GET':
        return render(request,'Portfolio.html')
    if request.method=='POST':
        name = request.POST['name']
        subject  = request.POST['text']
        message = "You have a Mail from your Portfolio by: - " + name + " (" + str(request.POST['email']) + ")\n\n" 
        message = message + (request.POST['message'])
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['prabal.pandey.prabal@gmail.com',]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'Portfolio.html')