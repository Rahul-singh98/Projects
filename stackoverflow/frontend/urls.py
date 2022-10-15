from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ask', views.ask, name='ask'),
    path('question/<int:question_id>', views.question, name="question"),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
]