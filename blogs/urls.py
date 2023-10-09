from django.urls import path, include
from blogs.views import ListBlogView, DetailBlogView, CreateBlogView, DeleteBlogView, UpdateBlogView

urlpatterns = [
    # blogs top is <http://127.0.0.1:8000/blogs/>
    path('', ListBlogView.as_view(), name='blogList'),
    path('detail/<int:pk>/', DetailBlogView.as_view(), name='blogDetail'),
    path('create/', CreateBlogView.as_view(), name='blogCreate'),
    path('delete/<int:pk>/', DeleteBlogView.as_view(), name='blogDelete'),
    path('update/<int:pk>/', UpdateBlogView.as_view(), name='blogUpdate'),
]
