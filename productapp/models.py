from tkinter import CASCADE
from unicodedata import category
from django.db import models

#Specify your choices



# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_description = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.CharField(max_length=100)
    category_name = models.ForeignKey(Category,on_delete=models.CASCADE)
    product_image = models.ImageField(blank = True,upload_to = 'images/')
    product_description = models.CharField(max_length=500)
    size = (('Unavailable','Unavailable'),
            ('6','6'),
            ('7','7'),
            ('8','8'),
            ('9','9'),
            ('10','10'))
    product_size = models.CharField(max_length=50,choices=size)
    product_brand = models.CharField(max_length=100)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product_name
    
    @property
    def imageURL(self):
        try:
            url = self.product_image.url
        except:
            url = " "
        return url