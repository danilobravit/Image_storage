from django.contrib import admin
from django.urls import path 
from .views import ImageList, ImageDetails, ImageDownload
from django.conf.urls.static import static
from storage import settings

urlpatterns = [
    path('', ImageList.as_view()),
    path('<int:id>', ImageDetails.as_view()),
    path('<int:id>/download', ImageDownload.as_view()),
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)