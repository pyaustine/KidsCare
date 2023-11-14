from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('autism', include('autismApp.urls')),
    # path('api', include('api.urls')),
]
