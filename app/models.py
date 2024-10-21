from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='images/')
    stock=models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.name
    
class CartItem(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} X {self.product.name}"
    
    
    def get_total_price(self):
        return self.quantity * self.product.price