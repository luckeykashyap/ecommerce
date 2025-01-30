from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from order.models import Order

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_STATUS = (
        ('PENDING', 'Pending'),
        ('SUCCESS', 'Success'),
        ('FAILED', 'Failed'),
        ('CANCELLED', 'Cancelled'),
    )
    payment_status = models.CharField(max_length=50, choices=PAYMENT_STATUS, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    PAYMENT_METHOD = (
        ('COD', 'Cash On Delivery'),
        ('CARD', 'Credit Card'),
        ('CASH', 'Cash'),
        ('MOBILE PAYMENT', 'Mobile Payment'),
        ('BANK TRANSFER', 'Bank Transfer'),
    )
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, default='COD')

    def __str__(self):
        return f"{self.user} - {self.amount}: {self.payment_status}-> {self.payment_method}"
