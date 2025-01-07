from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def add_product(request):
    if request.method == "POST":
        name = request.POST['name']
        category = request.POST['category']
        quantity = int(request.POST['quantity'])
        Product.objects.create(name=name, category=category, quantity=quantity)
        return redirect('product_list')
    return render(request, 'inventory/add_product.html')

def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        product.name = request.POST['name']
        product.category = request.POST['category']
        product.quantity = int(request.POST['quantity'])
        product.save()
        return redirect('product_list')
    return render(request, 'inventory/update_product.html', {'product': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product_list')

def reduce_quantity(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        reduce_by = int(request.POST['reduce_by'])
        product.quantity = max(0, product.quantity - reduce_by)
        product.save()
        return redirect('product_list')
    return render(request, 'inventory/reduce_quantity.html', {'product': product})
