from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('post-todo/', post_todo, name='post_todo')
]