from django.urls import path

from catalog.views import product_details_view, ProductListView

app_name = 'catalog'

urlpatterns = [
    path('<int:product_id>/', product_details_view, name='detail'),
    path('list/', ProductListView.as_view(), name='list'),
]