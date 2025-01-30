# Generated by Django 5.1.5 on 2025-01-30 16:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('DELIVERED', 'Delivered'), ('CANCELLED', 'Cancelled'), ('SHIPPED', 'Shipped'), ('OUT FOR DELIVERY', 'Out for Delivery')], default='PENDING', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payment_method', models.CharField(choices=[('COD', 'Cash On Delivery'), ('CARD', 'Credit Card'), ('CASH', 'Cash'), ('MOBILE PAYMENT', 'Mobile Payment'), ('BANK TRANSFER', 'Bank Transfer')], default='COD', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
