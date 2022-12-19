# THIS FILE IS TO  GENERATE WHAT THE USER SEES

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

'''
Function view: 
  - HttpResponse('str') returns string
  - render(request, 'app/index.html') returns a template
'''
def index(request):
  # return HttpResponse('Hello, Django')
  return render(request, 'django_intro/index.html')

def ray(request):
  return HttpResponse('Hello, Ray')

def xavier(request):
  return HttpResponse('Hello, Xavier')

# Greet function w/ context
def greet(request, name):
  return render(request, 'django_intro/greet.html', {'name': name.capitalize()})
