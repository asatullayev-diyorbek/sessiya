from django.urls import path
from main import views

app_name = 'main'
urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
]
