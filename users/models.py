from django.db import models

# Create your models here.
class Company(models.Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email