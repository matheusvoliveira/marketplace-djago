from django.db import models
from .models import models 
# Create your models here.

class Products(models.Model):
    product = models.CharField(max_length=50)
    value = models.FloatField(default=0)
    image = models.ImageField()
    
    def __str__(self):
        return self.product
    