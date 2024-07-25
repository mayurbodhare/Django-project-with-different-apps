from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
# from .templates import email
# Create your views here.

def form(request):
    return render(request,'email/form.html')


def send(request):
    if request.method == 'POST':
        subject = str(request.POST["subject"])
        message = str(request.POST["message"])
        recipient = str(request.POST["recipient"])
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [recipient]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'email/success.html')
        # return HttpResponse("sent")

