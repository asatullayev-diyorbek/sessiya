from django.conf.urls.static import static
from django.urls import path, include

from config import settings
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
