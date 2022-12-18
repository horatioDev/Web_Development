from django.urls import path

from . import views

# Handling name-spacing errors
app_name = 'tasks'
urlpatterns = [
  path('', views.index, name='index'),
  path('add', views.add, name='add')
]