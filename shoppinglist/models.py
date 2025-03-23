from django.db import models

class ShoppingItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    added_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.quantity})"
