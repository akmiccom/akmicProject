from django.urls import path, include
from calculator.views import ProductListView, calculatorPlus

urlpatterns = [
    path('products/', ProductListView.as_view(), name='productList'),
    path('caluPlus/', calculatorPlus, name='calcPlus')
    # path('csv/upload', CsvUploadView.as_view(), name='csvUpload'),
]
