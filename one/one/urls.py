
from django.contrib import admin
from django.urls import path
from api.views import get_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api", get_info)
]
