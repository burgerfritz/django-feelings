from django.conf.urls import include
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
