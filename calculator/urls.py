from django.urls import path, include
from calculator.views import CalculatorView
# from calculator.views import ProductListView

urlpatterns = [
    path('', CalculatorView.as_view(), name='calculator'),
    # path('products/', ProductListView.as_view(), name='productList'),
]
