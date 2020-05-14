from datetime import datetime

from django.shortcuts import render,HttpResponse


# Create your views here.
#from myapp.models import Contact
from .models import booking


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'index.html')


def aboutUs(request):
    return render(request, 'aboutUs.html')


def menu(request):
    return render(request, 'menu.html')


def reservations(request):
    return render(request, 'reservations.html')


def contact(request):

    if request.method == "POST":
        name=request.POST.get('name')
        email = request.POST.get('email')
        subject= request.POST.get('subject')
        message = request.POST.get('message')
        contact=booking(name=name,email=email,subject=subject,message=message)

        contact.save()

    return render(request, 'contact.html')


def gallery(request):
    return render(request, 'gallery.html')
