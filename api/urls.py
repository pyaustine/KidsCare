from django.urls import path
from django.urls import re_path as url, path, include
from rest_framework import permissions

from . import views
from .views import predictAPIView

api_patterns = [
    path('test/', views.testEndpoint, name='test'),
    path('predict/', predictAPIView.as_view(), name='predict')
]

urlpatterns = [
    url(r'^$', views.getRoutes, name='routes'),
    url(r'^', include(api_patterns)),
]