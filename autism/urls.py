from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('', include('admin_soft.urls')),
    path('admin/', admin.site.urls),
    path('', include('autismApp.urls')),
    path('api/', include('api.urls')),
    path('book-appointment/', include('appointment.urls')),
]
