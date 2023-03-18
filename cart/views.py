from django.shortcuts import render
from django.views.generic import ListView

from catalog.models import Product


# Create your views here.
class CartListView(ListView):
    model = Product
    template_name = 'cart/cart.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        return context

