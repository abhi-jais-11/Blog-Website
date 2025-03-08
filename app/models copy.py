from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class PostModel(models.Model):
    title=models.CharField(max_length=80)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField(blank=False)
    is_publish=models.BooleanField(default=False)
    like=models.IntegerField(default=0)
    create_at=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=200,blank=True)
    image=models.ImageField(null=True)
    
    def __str__(self):
        return self.title

class BannerModel(models.Model):
    title=models.CharField(max_length=80)
    author=models.CharField(max_length=50)
    body=models.TextField()
    is_publish=models.BooleanField(default=False)
    like=models.IntegerField(default=0)
    create_at=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=200,blank=True)
    image=models.ImageField(upload_to='media/', null=True, blank=True)
    
    def __str__(self):
        return self.title



class ConatactList(models.Model):
    title=models.CharField(max_length=200)
    contact=models.CharField(max_length=325)
    url=models.CharField(max_length=500)
    
    def __str__(self):
        return self.title
    

class ContactUs(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.CharField(max_length=50)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    
    
    def __str__(self):
        return self.name 
    