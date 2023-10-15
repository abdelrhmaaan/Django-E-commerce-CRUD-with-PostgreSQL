from django.db import models

# Create your models here.

class Product(models.Model):
    # design your product detials as you want 
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to='',default='media/images/pic2.jpg')
    inStock_choices = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    inStock = models.CharField(max_length=3,choices=inStock_choices,default='yes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'
