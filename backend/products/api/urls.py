from django.urls import path
from .views import ProductAV, ProductDetailAV

urlpatterns = [
    path('list/', ProductAV.as_view(), name="product_list"),
    path('<int:pk>/', ProductDetailAV.as_view(), name="product_detail")
]