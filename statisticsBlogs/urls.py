from django.urls import path, include
from statisticsBlogs.views import ListStatisticsBlogView, DetailStatisticsBlogView, CreateStatisticsBlogView, UpdateStatisticsBlogView

urlpatterns = [
    path('', ListStatisticsBlogView.as_view(), name='statisticsList'),
    path('detail/<int:pk>/', DetailStatisticsBlogView.as_view(), name='statisticsDetail'),
    path('create/', CreateStatisticsBlogView.as_view(), name='statisticsCreate'),
    path('update/<int:pk>/', UpdateStatisticsBlogView.as_view(), name='statisticsUpdate'),
    path('delete/<int:pk>/', DetailStatisticsBlogView.as_view(), name='statisticsDelete'),
]
