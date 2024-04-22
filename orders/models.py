from django.db import models
from decimal import Decimal
from account.models import User
from products.models import ProductVariant
from project.constant import STATUS_CHOICES

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    shipping_address = models.TextField(default="")
    comments = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order {self.id} - {self.user.first_name}"
    
    # def calculate_total_price(self):
    #     total_price = self.items.aggregate(total_price=Sum(models.F('quantity') * models.F('price')))['total_price']
    #     return total_price if total_price is not None else 0.0

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, default="")
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.quantity} x {self.product_variant.product.name} in Order {self.order.id}"
    
    def calculate_subtotal(self):
        price = Decimal(str(self.product_variant.product.price)) 
        discount = Decimal(str(self.product_variant.product.discount))  
        subtotal = self.quantity * price * (1 - discount / Decimal(100))
        return subtotal
    
