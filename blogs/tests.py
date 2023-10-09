from django.test import TestCase

# Create your tests here.
# from blogs.models import Blog
from glob import glob
import os
import re

files = glob(r'blogs/markdown/*.md')

for file in files:
    print(os.path.basename(file))
    
# Blogモデルに外部markdownからテキストを追加
def readMarkdown(file):
    # read markdown and output title, text
    with open(file, encoding='utf-8', mode='r') as f:
        result = f.readlines()
        title = [t.rstrip() for t in result if '# ' in t][0].replace('# ', '')
        author = [t.rstrip() for t in result if 'Author : ' in t][0].replace('Author : ', '')
        category = [t.rstrip() for t in result if 'Category : ' in t][0].replace('Category : ', '')
        text = '\n'.join([t.rstrip() for t in result if re.search(r'^(?!# ).+$', t)])
    return title, category, author, text

for file in glob(r'blogs/markdown/*.md'):
    title, category, author, text = readMarkdown(file)


# def create_items(request):
# items_to_create = [
#     Blog(title='test1', author='aaa'),
#     Blog(title='test2', author='bbb'),
# ]
    
# Blog.objects.bulk_create(items_to_create)