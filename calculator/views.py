from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from calculator.models import Calculator
from calculator.forms import CalculatorForm

from glob import glob
import csv


class CalculatorListView(ListView):
    model = Calculator
    template_name = 'calculator/calculatorList.html'
    context_object_name = 'calculatorList'
    

class CalcSimpleView(View):
    model = Calculator
    template_name = 'calculator/SimpleCalculator.html'

    def get(self, request):
        form = CalculatorForm()
        result = None
        params = {
            'title': 'Simple Calculator',
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
