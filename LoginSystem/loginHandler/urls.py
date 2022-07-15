from django.urls import path
from . import views

urlpatterns = [
    path('login', views.handlelogin, name='login'),
    path('signup', views.signup, name='signup'),
    path('', views.home, name='home')
]
