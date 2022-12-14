from django.db import models

# Create your models here.

class Subscriber(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.DateField()
    email=models.EmailField()
    password=models.CharField(max_length=50)
    cpassword=models.CharField(max_length=50)
    


    def __str__(self):
        return self.fname+' '+self.lname+' '+self.email    


