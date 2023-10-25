from django.urls import path, include
from calculator.views import CalculatorListView, CalcSimpleView


urlpatterns = [
    path('', CalculatorListView.as_view(), name='calculatorList'),
    path('simpleCalculator', CalcSimpleView.as_view(), name='SimpleCalculator'),
    path('comlexCalculator', CalcSimpleView.as_view(), name='ComplexCalculator'),
    # path('products/', ProductListView.as_view(), name='productList'),
]
