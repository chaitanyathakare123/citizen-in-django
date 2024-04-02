from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()
    def __str__(self):
        return self.name
class Complaint(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    name = models.CharField(max_length=100)
    title= models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField()
    urgency = models.CharField(max_length=50)
    latitude = models.FloatField(default=0.0)
    longitude = models.FloatField(default=0.0)
    attachments = models.FileField(upload_to='static/', null=True, blank=True)

    def _str_(self):
        return self.name
