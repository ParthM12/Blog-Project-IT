from django.db import models
class text123(models.Model):
    text=models.TextField()
# Create your models here.
class comment1(models.Model):
    text=models.TextField()
    Date=models.DateTimeField(auto_now=True)