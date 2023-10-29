from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)
    
class Offer(models.Model):
    code = models.CharField(max_length=16)
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Offer2(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.CharField(max_length=2500)

class Buy(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    
   


class new_user(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    pincode=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    job=models.CharField(max_length=200)
    password=models.CharField(max_length=200)


class new_user1(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    landmark=models.CharField(max_length=200)

    password=models.CharField(max_length=200)

class Buy2(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    username=models.CharField(max_length=200)
    email=models.EmailField()
    phone=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    landmark=models.CharField(max_length=200)
   

