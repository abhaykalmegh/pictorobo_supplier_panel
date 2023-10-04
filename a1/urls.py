from django.urls import path
# from .views import create_product, list_products, product_upload
from .views import product_upload
from .views import CreateProduct, ListProducts


urlpatterns = [
    # path('products/create/', create_product, name='create-product'),
    path('products/create/', CreateProduct.as_view(), name='create-product'),
    # path('products/', list_products, name='list-products'),
    path('products/', ListProducts.as_view(), name='list-products'),
    path('products/upload/', product_upload, name='product-upload'),
]