from django.db import models

# Create your models here.

# => add category  make new class 
# has name , desc , image , created_at , updated_at
# link product with category 

class Category(models.Model):
    name = models.CharField(max_length=100,null=True)
    desc = models.CharField(max_length=500,null=True,blank=True)
    image = models.ImageField(upload_to='category/', default='media/images/pic2.jpg',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'


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
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)

    def __str__(self) -> str:
        return f'{self.name}'



