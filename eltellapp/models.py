from django.db import models

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    role=models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Worker(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phonenumber=models.IntegerField()
    works=models.CharField(max_length=100)
    perhour=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)

class Marketing(models.Model):
    file = models.FileField(upload_to=None, max_length=254)    
    description=models.CharField(max_length=2000)

class Logo(models.Model):
    file = models.FileField(upload_to=None, max_length=254)    
    description=models.CharField(max_length=2000)    
class App(models.Model):
    file = models.FileField(upload_to=None, max_length=254)    
    description=models.CharField(max_length=2000)    

class Designer(models.Model):
    file=models.FileField(upload_to=None, max_length=254)
    description=models.CharField(max_length=2000)   