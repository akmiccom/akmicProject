from django import forms
from statisticsBlogs.models import StatisticsBlog


class StatisticsBlogForm(forms.Form):
    class Meta:
        model = StatisticsBlog
        fields = ('chapter', 'section', 'title', 'text')