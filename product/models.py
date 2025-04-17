from django.db import models

# Create your models here.
class ProductTable(models.Model):
    image = models.ImageField(upload_to='media/productimage/')
    name = models.CharField(max_length=20,blank=False)
    quantity = models.CharField(max_length=10,blank=True)
    price = models.CharField(max_length=5,blank=False)

    def __str__(self):
        return self.name + self.quantity
