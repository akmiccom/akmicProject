from django import forms


class CalcPlusForm(forms.Form):
    value1 = forms.IntegerField(label='1つ目の数値')
    value2 = forms.IntegerField(label='2つ目の数値')