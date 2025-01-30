from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    ORDER_STATUS = (
        ('PENDING', 'Pending'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
        ('SHIPPED', 'Shipped'),
        ('OUT FOR DELIVERY', 'Out for Delivery'),
    )
    order_status = models.CharField(max_length=50, choices=ORDER_STATUS, default='PENDING')
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
        return f"{self.user} - {self.total_amount}: {self.order_status}-> {self.payment_method}"