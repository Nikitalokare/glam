from django.db import models
from AdminApp.models import products
from datetime import datetime
from django  import forms

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)

    class Meta:
        db_table = "UserInfo"

class Mycart(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    product = models.ForeignKey(products,on_delete=models.CASCADE)
    qunt = models.IntegerField(default=1)
    shade = models.CharField(max_length=20,default="No shade")
    class Meta:
        db_table = "Mycart"

class OrderMaster(models.Model):
    user = models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    date_of_order = models.DateField(default = datetime.now)
    amount = models.FloatField(default=1000)
    details = models.CharField(max_length=200)
    shades = models.CharField(max_length=100,default="No shade")
    class Meta:
        db_table = "OrderMaster"

class fileupload(models.Model):
    '''file = models.FileField()'''
    file=models.FileField()

    class Meta:
        db_table = "fileupload"
        


