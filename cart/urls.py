from django.urls import path

from cart.views import CartListView

app_name = 'cart'

urlpatterns = [
    path('', CartListView.as_view(), name='cart'),
]