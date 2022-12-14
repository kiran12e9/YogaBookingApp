from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model=Subscriber
        fields=['fname','lname','email','password','cpassword','dob']
        