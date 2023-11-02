from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from statisticsBlogs.models import StatisticsBlog

from statisticsBlogs.functions import updata_or_create_markdown
import os


title = 'Statistics blogs'
header_h1 = '統計学の基本について紹介します'
header_p = '統計学は私たちの日常生活や科学のさまざまな分野で役立っています。'

class ListStatisticsBlogView(ListView):
    model = StatisticsBlog
    ordering = ('chapter', 'section')
    template_name = 'statisticsBlogs/statisticsList.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = title
        context['header_h1'] = header_h1
        context['header_p'] = header_p
        context['counterFotIf'] = [f'{i+1:02}' for i in range(15)]
        return context

class DetailStatisticsBlogView(DetailView):
    model = StatisticsBlog
    template_name = 'statisticsBlogs/statisticsDetail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = title
        context['header_h1'] = header_h1
        context['header_p'] = header_p
        return context
    
class UpdateStatisticsBlogView(UpdateView):
    model = StatisticsBlog
    fields = ('chapter', 'section', 'title', 'text')
    template_name = 'statisticsBlogs/statisticsUpdate.html'
    success_url = reverse_lazy('statisticsList')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = title
        context['header_h1'] = header_h1
        context['header_p'] = header_p
        return context

class DeleteStatisticsBlogView(DeleteView):
    model = StatisticsBlog
    template_name = 'statisticsBlogs/statisticsDelete.html'
    success_url = reverse_lazy('statisticsList')
    
class CreateStatisticsBlogView(CreateView):
    model = StatisticsBlog
    fields = ('chapter', 'section', 'title', 'text')
    template_name = 'statisticsBlogs/statisticsCreate.html'
    success_url = reverse_lazy('statisticsList')


# update or create on specified folder
markdown_dir = os.path.join(settings.BASE_DIR, 'statisticsBlogs', 'markdown')
updata_or_create_markdown(markdown_dir)
    
# with open(r'statisticsBlogs\csv\統計学入門.csv', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         # update_or_create
#         StatisticsBlog.objects.update_or_create(
#             chapter=row[0],
#             section=row[1],
#             defaults={
#                 'title': row[2],
#                 },
#             )
