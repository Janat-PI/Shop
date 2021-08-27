from django.urls import path
from django.contrib.auth.views import LogoutView
from django.views.decorators.cache import cache_page
from .views import *


urlpatterns = [
    path('', BaseView.as_view(), name='base'),
    path('products/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('category/<str:slug>/', cache_page(280)(CategoryDetailView.as_view()), name='category_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:slug>/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove-from-cart/<str:slug>/', DeleteFromCartView.as_view(), name='delete_from_cart'),
    path('change-qty/<str:slug>/', ChangeQTYView.as_view(), name='change_qty'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('make-order/', MakeOrderView.as_view(), name='make_order'),
    path('login/', cache_page(300)(LoginView.as_view()), name='login'),
    path('logout/', cache_page(500)(LogoutView.as_view(next_page="/")), name='logout'),
    path('registration/', cache_page(500)(RegistrationView.as_view()), name='registration'),
    path('payed-online-order/', PayedOnlineOrderView.as_view(), name='make_order'),
    path('add-favorite/<int:id>/', addtofavorite, name='add-to-favorite'),
    path('favorites/', prouct_favorite, name='product_favorite')
]
