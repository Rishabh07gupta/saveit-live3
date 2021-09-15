from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="Customer")
    name = models.CharField(max_length=30, null=True)
    phone = models.CharField(max_length=12, null=True)
    date_added = models.DateTimeField(verbose_name='date added',null=True,auto_now_add=True)
    #due = models.CharField(max_length=10, null=True, blank=True)
    Address = models.CharField(name="address", max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.name)



class Collection(models.Model):
    CATEGORY = (
        ('Paid', 'Paid'),
        ('Unpaid', 'Unpaid'),
    )


    Amount = models.IntegerField(name='amount', null=True)
    date = models.DateField(name='date', auto_now_add=False, auto_now=False, blank=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    description = models.CharField(max_length=500 , null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.customer)
    


