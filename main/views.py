from django.shortcuts import render,redirect
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.

def home_page(request):
    context = {}
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        cn=Contact(name=name, email=email, message=message)
        cn.save()
        messages.success(request,'Thank you! Your message has been submitted.')
        # Send email to YOU
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Sender: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['patidarvrashti2005@gmail.com'],  # Replace with your email
            fail_silently=False,
         )
         # Send auto-reply to USER
        send_mail(
            subject='Thanks for contacting us!',
            message=f"Hi {name},\n\nThank you for reaching out! We have received your message and will get back to you shortly.\n\nRegards,\nVrashti",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email],  # user's email
            fail_silently=False,
         )
        return render(request,'main/success.html')
    else:
        return render(request,'main/home.html')