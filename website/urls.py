from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('produitDetails/', views.produitDetails, name="produitDetails"),
    path('shop/', views.shop, name="shop"),
]
