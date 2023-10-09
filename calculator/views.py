from django.shortcuts import render

from django.views.generic import ListView
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
        'title': 'CalcPlus',
        'forms': CalcPlusForm(),
        'answer': 'Answer is ',
    }
    
    if request.method == 'POST':
        params['answer'] = f'Answer is {str(int(request.POST["value1"])) + str(int(request.POST["value2"]))}'
        params['forms'] = CalcPlusForm(request.POST)
        
        return render(request, 'calcutator/calcPlus.html', params)