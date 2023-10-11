from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from statisticsBlogs.models import StatisticsBlog
import csv


class ListStatisticsBlog(ListView):
    model = StatisticsBlog
    ordering = ('chapter', 'section')
    template_name = 'statisticsBlogs/statisticsList.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Statistics blogs'
        context['header_h1'] = 'This is a page of Statistics.'
        context['header_p'] = "We'll start from the basics, so let's do our best."
        return context


class DetailStatisticsBlog(DetailView):
    model = StatisticsBlog
    template_name = 'statisticsBlogs/statisticsDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_h1'] = 'This is a page of Statistics.'
        context['header_p'] = "We'll start from the basics, so let's do our best."
        return context
    

class DeleteStatisticsBlog(DeleteView):
    model = StatisticsBlog
    template_name = 'statisticsBlogs/statisticsDelete.html'
    success_url = reverse_lazy('statisticsList')
    
class CreateStatisticsBlog(CreateView):
    model = StatisticsBlog
    fields = ('chapter', 'section', 'title', 'text')
    template_name = 'statisticsBlogs/statisticsCreate.html'
    success_url = reverse_lazy('statisticsList')
    
class UpdateStatisticsBlog(UpdateView):
    model = StatisticsBlog
    fields = ('chapter', 'section', 'title', 'text')
    template_name = 'statisticsBlogs/statisticsUpdate.html'
    success_url = reverse_lazy('statisticsList')
    
    

with open(r'statisticsBlogs\csv\統計学入門.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        # update_or_create
        StatisticsBlog.objects.update_or_create(
            chapter=row[0],
            section=row[1],
            defaults={
                'title': row[2],
                },
            )
    
