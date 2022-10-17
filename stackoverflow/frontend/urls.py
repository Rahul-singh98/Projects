from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ask', views.ask, name='ask'),
    path('question/<int:question_id>', views.question, name="question"),
    path('profile/<int:user_id>', views.user_profile, name='profile'),
    path('login', views.loginView, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logoutView, name='logout'),
]

handler404 = 'frontend.views.error_404'
handler500 = 'frontend.views.error_500'