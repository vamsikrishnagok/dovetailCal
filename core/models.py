from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Dovetail(models.Model):
    sheetname = models.CharField(max_length=250,blank=True,null=True)
    leftArm = models.FloatField(default=0)
    rightArm = models.FloatField(default=0)
    depth = models.FloatField(default=0)
    width = models.FloatField(default=0)
    thickness = models.FloatField(default=0)
    centerDepth = models.FloatField(default=0)
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)

class Dowell(models.Model):
    sheetname = models.CharField(max_length=250,blank=True,null=True)
    leftArm = models.FloatField(default=0)
    rightArm = models.FloatField(default=0)
    depth = models.FloatField(default=0)
    width = models.FloatField(default=0)
    thickness = models.FloatField(default=0)
    centerDepth = models.FloatField(default=0)
    createdDate = models.DateTimeField()
    updatedDate = models.DateTimeField()
    createdBy = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)


class Cutsheet(models.Model):
    orderNo = models.CharField(max_length=250)
    trkWeight = models.FloatField()
    pallets = models.FloatField()
    orderDate = models.DateTimeField()
    shipDate = models.DateTimeField()
    totalBoxes = models.IntegerField()
    shippingInstructions = models.TextField()
    errNo = models.IntegerField()
    sideSQFT = models.FloatField()
    bottomSQFT = models.FloatField()
    createdDate = models.DateTimeField(blank=True,null=True)
    createdBy = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)