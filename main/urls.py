from django.urls import path
from main import views

urlpatterns = [
    path('', views.home, name='home'),
    path('shoes', views.shoes, name='shoes'),
    path('cart', views.cart, name='cart'),
    path('add-to-cart', views.add_to_cart, name='add_to_cart'),
    
    path('cart-items', views.GetCartItems.as_view(), name='GetCartItems'),

    path('shoes/<str:product_name>', views.product_detail, name='product_detail'),
]