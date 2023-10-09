from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from blogs.models import Blog
from markdown import Markdown
from glob import glob
import re

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
    # read markdown and output title, text
    with open(file, encoding='utf-8', mode='r') as f:
        result = f.readlines()
        title = [t.rstrip() for t in result if '# ' in t][0].replace('# ', '')
        author = [t.rstrip() for t in result if 'Author : ' in t][0].replace('Author : ', '')
        category = [t.rstrip() for t in result if 'Category : ' in t][0].replace('Category : ', '')
        allText = [t.rstrip() for t in result if re.search(r'^(?!# ).+$', t)]
        pos = allText.index('## note')
        markdownText = '\n'.join(allText[:pos])
        md = Markdown(extensions=['extra'])
        text = md.convert(markdownText)
        
    return title, category, author, text

for file in glob(r'blogs/markdown/*.md'):
    title, category, author, text = readMarkdown(file)
    # update_or_create
    Blog.objects.update_or_create(
        title=title,
        author=author,
        category=category,
        defaults={
            'text': text,
            },
        )
