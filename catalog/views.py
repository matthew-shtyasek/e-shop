from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from .forms import Product2CartForm
from .models import Product


def product_details_view(request, product_id):
    prod = get_object_or_404(Product, id=product_id)
    cart = Cart(request)

    if request.method == 'POST':
        form = Product2CartForm(request.POST)
        if form.is_valid():
            # count = form.cleaned_data['count']
            cart[str(product_id)] = form.cleaned_data['count']
            form = Product2CartForm()
    else:
        form = Product2CartForm()

    if str(product_id) in cart.session['cart'].keys():
        in_cart = f'Добавлено в корзину {cart[str(product_id)]} шт.'
    else:
        in_cart = None

    context = {'product': prod,  # product = prod
               'form': form,
               'in_cart': in_cart}
    return render(request, 'catalog/product_details.html', context)


def product_list_view(request):
    products = Product.objects.all()
    objects_count = Product.objects.count()
    context = {'product_list': products, 'objects_count': objects_count}
    print(dict(request.session))
    return render(request, 'catalog/product_list.html', context)