import email
from pyexpat import model
from django.db import models

# Create your models here.
class Employee(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=70)
    salary=models.IntegerField()
    city=models.CharField(max_length=20,default=None,null=True ,blank=True)
    state=models.CharField(max_length=20,default=None,null=True ,blank=True)
    
    
    
    def __str__(self):
        return str(self.id)+" "+self.name
