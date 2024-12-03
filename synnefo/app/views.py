from django.shortcuts import render
import os
from app.models import Contact

from .models import *
# Create your views here.

def home(req):
    return render(req,'home.html')
def about(req):
    return render(req,'about.html')
def courses(req):
    data=Courses.objects.all()
    return render(req,'courses.html',{'courses':data}) 
def placement(req):
    data=Placement.objects.all()
    return render(req, 'placement.html', {'placements': data})
def contact(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        phone = req.POST['phone']
        message = req.POST['message']
        print(name, email, phone,message)
        try:
            data = Contact.objects.create(name=name,email=email,phone=phone,message=message)
            data.save()
            return render(req, 'contact.html')
        except Exception as e:
            return render(req,'contact.html')
    return render(req,'contact.html')