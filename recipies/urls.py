from django.urls import path
from recipies import views

urlpatterns = [
    path('', views.index, name='recipes_home'),
    path('recipe/<int:pk>', views.show, name='recipes_show'),
    path('recommend', views.recommend, name='recipes_recommend'),
    path('create', views.create, name='recipes_create'),
]