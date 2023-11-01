from django.urls import path
from mdToHtml.views import DetailMdToHtmlListView, DetailMdToHtmlDetailView


urlpatterns = [
    path('', DetailMdToHtmlListView.as_view(), name='list'),
    path('detail/<int:pk>', DetailMdToHtmlDetailView.as_view(), name='detail')
]
