from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home',views.home),
    path('signup',views.signup),
    path('login',views.login),
    path('forgotpassword',views.forgotpassword),
    path('subscription',views.subscriptiondetails),
    path('subscribe',views.subscribe),
    path('history',views.history),
    path('editinfo',views.editinfo),
    path('logout',views.logout),
    path('history',views.history)
    
    
]
