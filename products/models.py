from django.db import models



cat_type_choices = (('HOT_BEVERAGES','Hot Beverages'),('COLD_BEVERAGES','Cold Beverages'),('SOFT_DRINKS','Soft Drinks'),('FRESH_JUICES','Fresh Juices'),('SNACKS','Snacks'))

class Category(models.Model):
    c_name = models.CharField(max_length=200)
    description = models.TextField()
    category_type = models.CharField(max_length=50, choices=cat_type_choices, default='HOT_BEVERAGES')

    def __str__(self):
        return f"{self.c_name} - {self.category_type}"

class Product(models.Model):
    p_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='products/')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.p_name} - {self.category}: {self.price}-> {self.stock} in stock"

    