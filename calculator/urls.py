from django.urls import path, include
from calculator.views import CalculatorListView, CalculatorView
# from calculator.views import ProductListView

urlpatterns = [
    path('', CalculatorListView.as_view(), name='calculatorList'),
    path('calculator/<int:pk>/', CalculatorView.as_view(), name='simpleCalculator'),
    # path('products/', ProductListView.as_view(), name='productList'),
]
