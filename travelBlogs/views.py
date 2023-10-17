from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from travelBlogs.models import TravelBlog
from glob import glob
import re
import os


TILTE = 'Travel Blog'
HEADER_H1 = 'Travel Blog'
HEADER_P = '楽しく書いていきます'

class ListTravelBlogView(ListView):
    model = TravelBlog
    template_name = 'travelBlogs/travelBlogList.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TILTE
        context['header_h1'] = HEADER_H1
        context['header_p'] = HEADER_P
        context['counterFotIf'] = [f'{i+1:02}' for i in range(13)]
        return context
    
class DetailTravelBlogView(DetailView):
    model = TravelBlog
    template_name = 'travelBlogs/travelBlogDetail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = TILTE
        context['header_h1'] = HEADER_H1
        context['header_p'] = HEADER_P
        context['counterFotIf'] = [f'{i+1:02}' for i in range(13)]
        return context


   
def readMarkdown(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = [t.strip() for t in f.readlines()]
        start, end = [i for i, t in enumerate(lines) if re.search(r'^-{3}', t)]
    # Markdownファイルからメタデータを抽出
    metadata = {
        'text': '\n'.join(lines[end+1:]),
        }
    metadata_lines = lines[start+1:end]
    for metadata_line in metadata_lines:
        key, value = metadata_line.split(':')
        metadata[key.strip().lower()] = value.strip().lower()
    return metadata
    
markdown_dir = os.path.join(settings.BASE_DIR, 'travelBlogs', 'markdown')
for file in glob(f'{markdown_dir}/*.md'):
    metadata = readMarkdown(file)
    # update_or_create
    TravelBlog.objects.update_or_create(
        title = metadata['title'],
        author = metadata['author'],
        category = metadata['category'],
        defaults={
            'text': metadata['text'],
            },
        )
