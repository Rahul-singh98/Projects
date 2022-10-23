from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.homepage, name='home'),
    path('ask', views.ask_question, name='ask'),
    path('question/<int:question_id>', views.view_question, name="question"),
    path('question/vote', views.handle_votes, name='votes'),
    path('comment/<int:question_id>', views.add_comment, name='comment'),
    path('answer/<int:question_id>', views.add_answer, name='answer'),
    path('profile/<int:user_id>', views.display_user_profile, name='profile'),
    path('login', views.handle_login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.handle_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'frontend.views.error_404'
handler500 = 'frontend.views.error_500'