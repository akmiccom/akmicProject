from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from calculator.models import Product
from calculator.forms import CalculatorForm

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

class CalculatorView(View):
    template_name = 'calculator/calculator.html'

    def get(self, request):
        form = CalculatorForm()
        result = None
        params = {
            'form': form,
            'result': result,
        }
        return render(request, self.template_name, params)

    def post(self, request):
        form = CalculatorForm(request.POST)
        result = None

        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            operator = form.cleaned_data['operator']
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Cannot divide by zero"

        params = {
            'title': 'Simple Calculator',
            'form': form,
            'result': result,
        }
        return render(request, self.template_name, params)
