from django.shortcuts import render, get_object_or_404
from .models import Product


def product_details_view(request, product_id):
    prod = get_object_or_404(Product, id=product_id)
    context = {'product': prod}  # product = prod
    return render(request, 'catalog/product_details.html', context)


def product_list_view(request):
    products = Product.objects.all()
    objects_count = Product.objects.count()
    context = {'product_list': products, 'objects_count': objects_count}
    return render(request, 'catalog/product_list.html', context)