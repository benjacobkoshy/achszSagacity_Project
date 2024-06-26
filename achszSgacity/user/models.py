from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    LIVE = 0
    DELETE = 0
    DELETE_CHOICES = ((LIVE,'Live'),(DELETE,'Delete'))

    name = models.CharField(max_length=200)
    #profle creation
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='customer_profile')

    #extra
    image = models.ImageField(upload_to='images/user_image/',null=True) 

    address = models.TextField()
    place = models.CharField(max_length=30)
    pin = models.CharField(max_length=10)
    dob = models.DateField(null=True)

    deleted_status = models.IntegerField(choices=DELETE_CHOICES ,default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


    def __str__(self)->str:
        return self.name