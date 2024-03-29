from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import *


urlpatterns = [
    path('', Index,name='index'),
    path('blog/', BlogHome, name='blog'),
    path('blog-details/<str:slug>/', PostDetail, name='post-details'),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)