from django.shortcuts import render, get_object_or_404

from .cart import Cart
from .forms import Product2CartForm
from .models import Product


def product_details_view(request, product_id):
    prod = get_object_or_404(Product, id=product_id)
    cart = Cart(request)

    if request.method == 'POST':
        form = Product2CartForm(request.POST)
        if form.is_valid():
            # count = form.cleaned_data['count']
            cart[product_id] = form.cleaned_data['count']
            form = Product2CartForm()
    else:
        form = Product2CartForm()

    context = {'product': prod,  # product = prod
               'form': form,
               'in_cart': product_id in cart.session['cart'].keys()}
    return render(request, 'catalog/product_details.html', context)


def product_list_view(request):
    products = Product.objects.all()
    objects_count = Product.objects.count()
    context = {'product_list': products, 'objects_count': objects_count}
    print(dict(request.session))
    return render(request, 'catalog/product_list.html', context)