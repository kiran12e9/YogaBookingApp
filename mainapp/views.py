from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'../Templates/home.html')

def index(req):
    return render(req,'../Templates/index.html')

def signup(req):
    return render(req,'../Templates/signup.html')    

def login(req):
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
