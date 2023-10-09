from django.urls import path, include
from calculator.views import ProductListView, calculatorPlus, CalculatorView

urlpatterns = [
    path('', calculatorPlus, name='calcPlus'),
    # path('', CalculatorView.as_view(), name='calcPlus'),
    path('products/', ProductListView.as_view(), name='productList'),
    # path('csv/upload', CsvUploadView.as_view(), name='csvUpload'),
]
