from django.db import models

class ShoppingItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (x{self.quantity})"

