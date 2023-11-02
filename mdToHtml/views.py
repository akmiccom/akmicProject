from django.shortcuts import render
from django.conf import settings
from django.views.generic import ListView, DetailView
from mdToHtml.models import MdToHtml
from glob import glob
import os
import re

from mdToHtml.functions import updata_or_create_markdown


class DetailMdToHtmlListView(ListView):
    model = MdToHtml
    template_name = 'mdToHtml/list.html'


class DetailMdToHtmlDetailView(DetailView):
    model = MdToHtml
    template_name = 'mdToHtml/detail.html'

markdown_dir = os.path.join(settings.BASE_DIR, 'statisticsBlogs', 'markdown')
updata_or_create_markdown(markdown_dir)