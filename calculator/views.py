from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from calculator.models import Product
from calculator.forms import CalcPlusForm

from glob import glob
import csv



class ProductListView(ListView):
    model = Product
    template_name = 'calculator/product_list.html'
    context_object_name = 'products'
    

csvFile = 'calculator/csv/sampleData.csv'
with open(csvFile, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        # update_or_create
        Product.objects.update_or_create(
            name=row['name'],
            price=row['price'],
            defaults={
                'description': row['description'],
                },
            )


def calculatorPlus(request):
    params = {
        'title': 'Calculator',
        'forms': CalcPlusForm(),
        'answer': '足し算の答え = ',
    }
    
    if request.method == 'POST':
        params['answer'] = f'{params["answer"]} {int(request.POST["value1"]) + int(request.POST["value2"])}'
        params['forms'] = CalcPlusForm(request.POST)
        
    return render(request, 'calculator/calcPlus.html', params)


class CalculatorView(View):
    def post(self, request):
        params = {
            'title': 'Calculator',
            'forms': CalcPlusForm(),
            'answer': '足し算の答え = ',
        }
        params['answer'] = f'{params["answer"]} {int(request.POST["value1"]) + int(request.POST["value2"])}'
        params['forms'] = CalcPlusForm(request.POST)
        
        return render(request, 'calculator/calcPlus.html', params)