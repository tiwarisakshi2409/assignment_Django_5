# models.py

from django.db import models

class ProductMst(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.product_id}: {self.product_name}"

class ProductSubCategory(models.Model):
    product = models.ForeignKey(ProductMst, on_delete=models.CASCADE)
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_images/')  # Use a relative path
    product_model = models.CharField(max_length=50)
    product_ram = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.product.product_name} - Model: {self.product_model}, RAM: {self.product_ram}"


# Create your models here.
