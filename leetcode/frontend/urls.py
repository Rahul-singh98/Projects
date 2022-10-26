from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('problems', views.add_code, name='add_code'),
]
