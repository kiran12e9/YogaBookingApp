
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .models import Subscriber
from .forms import SubscriberForm 
# Create your views here.
def home(req):
    return render(req,'../Templates/home.html')

def index(req):
    return render(req,'../Templates/index.html')

def signup(req):

    if req.method=='POST':

        form=SubscriberForm(req.POST or None)
        fname=req.POST.get('fname')
        lname=req.POST.get('lname')
        email=req.POST.get('email')
        password=req.POST.get('password')
        cpassword=req.POST.get('cpassword')
        dob=req.POST.get('dob')
        if(password==cpassword):
            if(form.is_valid()):
                form.save()
                return render(req,'../Templates/index.html')
        else:
            return render(req,'../Templates/forgotpassword.html')

    else:
        return render(req,'../Templates/signup.html')    
    
def login(req):
    if(req.method=='POST'):
        key=0
        temail=req.POST.get('email')
        tpassword=req.POST.get('password')
        if (Subscriber.objects.filter(email=temail, password=tpassword)).exists():
            a = Subscriber.objects.filter(email=temail).first()

            auth_login(req,a)
            return HttpResponse('Success')
        else:
            return HttpResponse('Login failed')    
    else:    
     return render(req,'../Templates/login.html')


def editinfo(req):
    return render(req,'../Templates/editinfo.html')


def subscribe(req):
    return render(req,'../Templates/subscribe.html')

def forgotpassword(req):
    return render(req,'../Templates/forgotpassword.html')


def subscriptiondetails(req):
    return render(req,'../Templates/subscriptiondetails.html')


def training(req):
    return render(req,'../Templates/training.html')


def history(req):
    return render(req,'../Templates/history.html')


def logout(req):
    return render(req,'../Templates/login.html')    
