from django.shortcuts import render, redirect
from .models import ShoppingItem
from .forms import ShoppingItemForm

def shopping_list(request):
    items = ShoppingItem.objects.all().order_by('-added_at')
    form = ShoppingItemForm()

    if request.method == 'POST':
        form = ShoppingItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shopping_list')

    return render(request, 'shopping_list.html', {'items': items, 'form': form})
