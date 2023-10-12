from django.shortcuts import render
from django.urls import reverse_lazy
from django.conf import settings
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from blogs.models import Blog
from markdown import Markdown
from glob import glob
import re
import os


class ListBlogView(ListView):
    model = Blog
    template_name = 'blogs/blogList.html'

class DetailBlogView(DetailView):
    model = Blog
    template_name = 'blogs/blogDetail.html'

class CreateBlogView(CreateView):
    model = Blog
    fields = ('title', 'text', 'category')
    template_name = 'blogs/blogCreate.html'
    success_url = reverse_lazy('blogList')
    
class UpdateBlogView(UpdateView):
    model = Blog
    template_name = 'blogs/blogUpdate.html'
    fields = ('title', 'text', 'category')
    success_url = reverse_lazy('blogList')

class DeleteBlogView(DeleteView):
    model = Blog
    template_name = 'blogs/blogDelete.html'
    success_url = reverse_lazy('blogList')


# Blogモデルに外部markdownからテキストを追加
def readMarkdown(file):
    with open(file, 'r', encoding='utf-8') as f:
        lines = [t.strip() for t in f.readlines()]
        start, end = [i for i, t in enumerate(lines) if re.search(r'^-{3}', t)]
    
    metadata = {}
    metadata_lines = lines[start+1:end]
    for metadata_line in metadata_lines:
        key, value = metadata_line.split(':')
        metadata[key.strip().lower()] = value.strip().capitalize()
    
    md = Markdown(extensions=['extra'])
    markdown = md.convert('\n'.join(lines[end+1:]))
        
    return metadata['title'], metadata['category'], metadata['author'], markdown

markdown_dir = os.path.join(settings.BASE_DIR, 'blogs', 'markdown')
for file in glob(f'{markdown_dir}/*.md'):
    title, category, author, text = readMarkdown(file)
    # update_or_create
    Blog.objects.update_or_create(
        title=title,
        author=author,
        defaults={
            'category': category,
            'text': text,
            },
        )
