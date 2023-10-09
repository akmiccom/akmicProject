from django.urls import path, include
from statisticsBlogs.views import ListStatisticsBlog, DetailStatisticsBlog, CreateStatisticsBlog, UpdateStatisticsBlog

urlpatterns = [
    path('', ListStatisticsBlog.as_view(), name='statisticsList'),
    path('detail/<int:pk>/', DetailStatisticsBlog.as_view(), name='statisticsDetail'),
    # path('create/', CreateStatisticsBlog.as_view(), name='statisticsCreate'),
    path('update/<int:pk>/', UpdateStatisticsBlog.as_view(), name='statisticsUpdate'),
    path('delete/<int:pk>/', DetailStatisticsBlog.as_view(), name='statisticsDelete'),
]
