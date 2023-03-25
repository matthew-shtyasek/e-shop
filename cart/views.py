from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import ListView

from cart.cart import Cart
from catalog.models import Product


# Create your views here.
class CartListView(ListView):
    model = Product
    template_name = 'cart/cart.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart = Cart(self.request)  # from cart.cart import Cart
        ids = list(map(int, list(cart.keys())))  # [1, 2, 3, 4]
        products = Product.objects.filter(id__in=ids)
        context[self.context_object_name] = products
        context['cart'] = self.request.session['cart']
        return context


def delete_from_cart(request, pk):
    if not request.is_ajax():
        raise PermissionDenied()
    cart = Cart(request)
    try:
        del cart[str(pk)]
    except KeyError as e:
        return JsonResponse({'successed': False})  # json serializable
    return JsonResponse({'successed': True})
