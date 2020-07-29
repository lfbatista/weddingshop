from django.db import models


class Product(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=False)
    brand = models.CharField(max_length=100, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    stock = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["created"]
