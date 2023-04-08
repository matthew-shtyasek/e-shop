from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

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


'''def product_list_view(request):
    products = Product.objects.all()
    objects_count = Product.objects.count()
    context = {'product_list': products, 'objects_count': objects_count}
    print(dict(request.session))
    return render(request, 'catalog/product_list.html', context)
'''


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'product_list'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)

        paginator = Paginator(self.object_list, self.paginate_by)
        try:
            page = self.request.GET.get('page')
        except:
            page = 1

        try:
            context[self.context_object_name] = paginator.page(page)
        except:
            context[self.context_object_name] = paginator.page(1)

        context['objects_count'] = self.model.objects.count()
        return context
