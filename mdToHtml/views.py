from django.shortcuts import render
from django.views.generic import ListView, DetailView

from mdToHtml.models import MdToHtml


class DetailMdToHtmlListView(ListView):
    
    model = MdToHtml
    template_name = 'mdToHtml/list.html'


class DetailMdToHtmlDetailView(DetailView):
    
    model = MdToHtml
    template_name = 'mdToHtml/detail.html'