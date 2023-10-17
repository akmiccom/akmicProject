from django.urls import path, include
from travelBlogs.views import ListTravelBlogView, DetailTravelBlogView

urlpatterns = [
    path('', ListTravelBlogView.as_view(), name='travelBlogList'),
    path('detail/<int:pk>', DetailTravelBlogView.as_view(), name='travelBlogDetail'),
]
