from django.urls import path

from cart.views import CartListView, delete_from_cart

app_name = 'cart'

urlpatterns = [
    path('', CartListView.as_view(), name='cart'),
    path('delete/<int:pk>/', delete_from_cart, name='delete'),
]