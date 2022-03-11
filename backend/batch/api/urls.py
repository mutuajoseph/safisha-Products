from unicodedata import name
from django.urls import path
from .views import BatchAV, BatchDetailAV

urlpatterns = [
    path('list/', BatchAV.as_view(), name="batch_list"),
    path('<int:pk>/', BatchDetailAV.as_view(), name="batch_details")
]