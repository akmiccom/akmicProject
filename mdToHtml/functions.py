from django.test import TestCase

from django.conf import settings
from mdToHtml.models import MdToHtml
from glob import glob
import os
import re

# Create your tests here.
def updata_or_create_markdown(markdown_dir):
    
    for file in glob(f'{markdown_dir}/*.md'):
        with open(file, 'r', encoding='utf-8') as f:
            fileName = os.path.splitext(os.path.basename(file))[0]
            chapter = fileName[:2]
            section = fileName[2:]
            lines = [t.strip() for t in f.readlines()]
            start, end = [i for i, t in enumerate(lines) if re.search(r'^-{3}', t)]
        metadata = {
        'chapter': chapter,
        'section': section,
        'markdown': '\n'.join(lines[end+1:]),
    }
        metadata_lines = lines[start+1:end]
        for metadata_line in metadata_lines:
            key, value = metadata_line.split(':')
            metadata[key.strip().lower()] = value.strip().lower()
        
        MdToHtml.objects.update_or_create(
        title = metadata['title'],
        defaults={
            'markdown': metadata['markdown'],
            },
    )
        
        
if __name__ == '__main__':
    markdown_dir = os.path.join(settings.BASE_DIR, 'statisticsBlogs', 'markdown')
    updata_or_create_markdown(markdown_dir)