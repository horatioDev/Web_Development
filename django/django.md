# Django

## Install Django
  - `pip3 install Django`

## Create Django Project
  - `django-admin startproject project_name`
    Ex: Google, Amazon

  ### Runserver
    - `py manage.py runserver`

## Create Django App
  - `py manage.py startapp app_name`
    Ex: Google Search | Images | Maps, Amazon Shopping | Videos

    ### Add app to project settings: project_name/settings.py

    ```
      INSTALLED_APPS = [
        'project_name', 
      ]
    ```

## Routes

  ### Create a view: app_name/views.py

  ```
    from django.shortcuts import render
    from django.http import HttpResponse

    # Create your views here.

    # Function view: 
    def index(request):
      return HttpResponse('Hello Django')
  ``` 
  
  ### Create a urls file app_name/urls.py

  ```
    # Import path to create url's
    from django.urls import path

    # Import views
    from . import views

    urlpatterns = [
      path('', views.index, name='index'),
    ]
  ```

  - #### Add app url's to project url's: project_name/urls.py
    ```
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('intro/', include('django_intro.urls')),
      ]
    ```

## Templates

  ### Create templates file structure
  - project_name/app_name/templates
    *Within the **templates** directory create another folder with the same name as app_name directory*

  - templates/app_name
    *Create template file*

  - templates/app_name/index.html
    ```
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <title>Templates Demo</title>
      </head>
      <body>
        <h1>Hello, Django</h1>
      </body>
      </html>
      
      <!-- Template w/ jinja syntax linked to view w/ context -->
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <title>Templates Demo</title>
      </head>
      <body>
        <h1>Hello, Django</h1>
      </body>
      </html>
    ```

    #### Link template to view
      ```
        def index(request):
          return render(request, 'django_intro/index.html')

        #View w/context
        def index(request):
          return render(request, 'django_intro/index.html', {'name': name.capitalize()})
      ```
  
  ### Template Inheritance

  - templates/app_name/base.html
    *A template w/ base structure for all files that inherits*

    ```
      <!-- Base Template Layout that all files inherits when used -->
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <title>Tasks Template</title>
      </head>
      <body> 
        <!-- Where content will differ on each page  -->
        {% block content %}

        {%% endblock}
      </body>
      </html>

      #Template that inherits 
      {% extends 'app_name/base.html' %}

      <!-- Where content will differ on each page  -->
      {% block content %}
        <ul>
          {% for item in items %}
            <li>{{ item }}</li>
          {% endfor %}
        </ul>
      {% endblock %}
    ```

## Static Files: CSS

  ### Create static file structure
  - project_name/app_name/static
    *Within the **static** directory create another folder with the same name as app_name directory*

  - static/app_name
    *Create dir/file* || *Create file*

  ### Link static files 
  ```
    <!-- Link Static files -->
    {% load static %}

    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>Is It New Year Template</title>
      <link rel="stylesheet" href="{% static 'new_year/css/styles.css' %}">
    </head>
  ```

## Forms
  - HTML Form: templates/app_name/form.html
    ```
      <h1>Add Task:</h1>
      <form action="{% url 'tasks:add' %}" method="post">
        {% csrf_token %}
        <input type="text" name="task">
        <input type="submit">
      </form>
      <a href="{% url 'tasks:index' %}">View Tasks</a>
    ```

  - Django Form: app_name/views.py
    ```
      from django.shortcuts import render

      # Import forms module
      from django import forms

      # Dummy List: context
      tasks = ['Create', 'Read', 'Update', 'Delete']

      # Django Form
      class NewTaskForm(forms.Form):
        # Input fields:
        # <input type='text' name='task' required id="id_task">
        task = forms.CharField(label='New Task')


      # Create your views here.
      def index(request):
        return render(request, 'tasks/index.html',
        {'tasks': tasks})

      # Add tasks view
      def add(request):
        return render(request, 'tasks/add.html', {'form': NewTaskForm()})
    ```

  - Django Form: templates/app_name/form.html
    ```
      <h1>Add Task:</h1>
      <form action="{% url 'tasks:add' %}" method="post">
        {% csrf_token %}
        {{ form }}
        <input type="submit" value="Submit">
        <a href="{% url 'tasks:index' %}">View Tasks</a>
      </form>
    ```

## Sessions
  - Sessions are generated per user