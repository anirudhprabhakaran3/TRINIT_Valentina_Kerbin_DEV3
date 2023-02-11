from django.urls import path
from pages import views


urlpatterns = [
    path('', views.home, name="pages_home"),
    path('register', views.signup, name='pages_signup'),
    path('profile', views.profile, name='pages_profile'),
]