from django.db import models
from account.models import User
from orders.models import Order
from project.constant import PAYMENT_MODE_CHOICES

class PaymentInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    payment_id = models.CharField(max_length=100) 
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_MODE_CHOICES, default='CREDIT_CARD')

    class Meta:
        verbose_name = 'Payment Information'
        verbose_name_plural = 'Payment Information'

    def __str__(self):
        return f"Payment for {self.user.first_name} - Amount: {self.payment_amount}"
    
