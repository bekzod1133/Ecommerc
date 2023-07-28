from django.urls import path
from . import views

urlpatterns=[
    path('',views.SHowProducts.as_view() , name='all_products'),
    path('cart/',views.CartDetail.as_view(), name='cart' ),
    path('<int:pk>/', views.addToCart, name='add_to_cart'),
]