from django.db import models

# Create your models here.

class login(models.Model):
    
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)


class empdata(models.Model):
    empid=models.IntegerField(primary_key=True)
    enum=models.IntegerField()
    empname=models.CharField(max_length=30)
    designation=models.CharField(max_length=130)
    specialization=models.CharField(max_length=30,null=True)
    doj=models.CharField(max_length=20)
    expsalary=models.IntegerField()
    prevexp=models.CharField(max_length=30)
    

class stockdata(models.Model):
    medicine=models.CharField(max_length=30)
    quantity=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    
    
    