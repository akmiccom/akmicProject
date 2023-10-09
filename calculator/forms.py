import pandas as pd
from django import forms
from calculator.models import Product


# class CsvUploadForm(forms.Form):
    
#     file = forms.FileField(label='csv file')
    
#     def save(self):
#         df = pd.read_csv(self['file'].value(), sep=',', encoding='utf-8')
#         df = df.fillna("")
#         rowIter = df.iterrows()
        
#         for row in rowIter:
#             row = row[1]
#             pk = row.get('id')
#             data = Product.objects.get(pk=pk)
#             data.name = row.get("name")
#             data.price = row.get("price")
#             data.description = row.get("description")
#             data.save()

class CalcPlusForm(forms.Form):
    value1 = forms.IntegerField()
    value2 = forms.IntegerField()