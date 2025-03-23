from django import forms
from .models import ShoppingItem

class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItemForm(forms.ModelForm):
        fields = ['name', 'quantity']
