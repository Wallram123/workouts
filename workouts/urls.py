from django.contrib import admin
from django.urls import path, include
from endpoints.views import index  # Import the view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('endpoints.urls')),
    path('', index),  # Root URL route
]
