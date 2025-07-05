from django.db import models

class Kond(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=15)
    image = models.ImageField(upload_to='kond-images/', blank=True, null=True, default='default/kond.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.model} {self.brand}"