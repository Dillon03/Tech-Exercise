from django.shortcuts import render, redirect
from .models import ShoppingItem

def shopping_list(request):
    if request.method == "POST":
        name = request.POST.get("name")
        quantity = request.POST.get("quantity")

        if name and quantity:
            ShoppingItem.objects.create(name=name, quantity=quantity)
        return redirect('/')

    items = ShoppingItem.objects.all()
    return render(request, "shoppinglist/list.html", {"items": items})

# Create your views here.
