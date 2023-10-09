from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.views import TopPageView

urlpatterns = [
    path('admin/', admin.site.urls), 
    
    path('', TopPageView.as_view(), name='topPage'),
    path('markdownx/', include('markdownx.urls')), 
    path('blogs/', include('blogs.urls')),
    path('statisticsBlogs/', include('statisticsBlogs.urls')),
    path('accounts/', include('accounts.urls')),
    path('calculator/', include('calculator.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

