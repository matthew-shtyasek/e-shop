from django.urls import path

from catalog.views import product_details_view, product_list_view

app_name = 'catalog'

urlpatterns = [
    path('<int:pk>/', product_details_view, name='detail'),
    path('list/', product_list_view, name='list'),
]