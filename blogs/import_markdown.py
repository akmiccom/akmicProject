import re
from glob import glob
from markdown import Markdown
from blogs.models import Blog



# Blogモデルに外部markdownからテキストを追加
def readMarkdown():
    for file in glob(r'blogs/markdown/*.md'):
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
        
        # update_or_create
        Blog.objects.update_or_create(
            title=title,
            author=author,
            category=category,
            defaults={
                'text': text,
                },
            )
    
if __name__ == '__main__':
    readMarkdown()