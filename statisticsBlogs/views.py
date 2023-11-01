from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from statisticsBlogs.models import StatisticsBlog
from markdown import Markdown
from glob import glob
import csv
import os
import re


title = 'Statistics blogs'
header_h1 = 'ここでは統計学の解説をしています'
header_p = "入門編ということにはなっていますが、少し難しい部分もあるかもしれません"

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
    
    
# タイトル一覧の作成
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
    

def readMarkdown(file):
    with open(file, 'r', encoding='utf-8') as f:
        fileName = os.path.splitext(os.path.basename(file))[0]
        chapter = fileName[:2]
        section = fileName[2:]
        lines = [t.strip() for t in f.readlines()]
        start, end = [i for i, t in enumerate(lines) if re.search(r'^-{3}', t)]
    # Markdownファイルからメタデータを抽出
    metadata = {
        'chapter': chapter,
        'section': section,
        'text': '\n'.join(lines[end+1:]),
    }
    metadata_lines = lines[start+1:end]
    # print(metadata_lines)
    for metadata_line in metadata_lines:
        key, value = metadata_line.split(':')
        metadata[key.strip().lower()] = value.strip().lower()
    # print(metadata)
    # md = Markdown(extensions=['extra'])
    # markdown = md.convert(text)
    
    return metadata
    
markdown_dir = os.path.join(settings.BASE_DIR, 'statisticsBlogs', 'markdown')
for file in glob(f'{markdown_dir}/*.md'):

    metadata = readMarkdown(file)
    # update_or_create
    StatisticsBlog.objects.update_or_create(
        chapter = metadata['chapter'],
        section = metadata['section'],
        title = metadata['title'],
        # author = metadata['author'],
        # category = metadata['category'],
        defaults={
            'text': metadata['text'],
            },
        )