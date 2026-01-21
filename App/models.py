from django.db import models
from django.utils import timezone

class User(models.Model):
    phone_number = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    house_number = models.CharField(max_length=10)
    street_name = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.CharField(max_length=10)
    user = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} - {self.last_name} - ({self.phone_number})"


class OTP(models.Model):
    phone_number = models.CharField(max_length=15)  # Store phone numbers as string
    otp = models.CharField(max_length=6)           # Assuming 6-digit OTP
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.phone_number} - {self.otp}"


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=0)
    reorder_threshold = models.IntegerField(default=10)
    image = models.ImageField(upload_to='products/', max_length=255, null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name