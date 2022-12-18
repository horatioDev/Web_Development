# THIS FILE IS USED TO  RENDER THE APP VIEWS

# Import path to create url's
from django.urls import path

# Import views
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  # # Custom route that adds name as an argument
  # path('<str:name>', views.greet, name='greet'),
  # path('ray/', views.ray, name='ray'),
  # path('xavier', views.xavier, name='xavier'),
]