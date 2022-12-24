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

## Routes / Url's

  ### Create a urls file app_name/urls.py
  - Flights App
    ```
      # FLights urls

      from django.urls import path

      from . import views

      urlpatterns = [
        path('', views.index, name='index'),
        path('<int:flight_id>', views.flight, name='flight'),
        path('<int:flight_id>/book', views.book, name='book'),
      ]
    ```

  - Users App
    ```
      # Users urls

      from django.urls import path

      from . import views

      urlpatterns = [
        path('', views.index, name='index'),
        path('login', views.login_view, name='login'),
        path('logout', views.logout_view, name='logout'),
      ]

    ```
  - #### Add app url's to project url's: project_name/urls.py
  - Flights App
    ```
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('flights/', include('flights.urls')),
      ]
    ```

  - Users App
    ```
      from django.contrib import admin
      from django.urls import path, include

      urlpatterns = [
          path('admin/', admin.site.urls),
          path('users/', include('users.urls')),
      ]

    ```

## Models
  - *After updating model makemigrations and migrate to update database*
  ### Create models for use in admin table
  - project_name/app_name/models.py
    ```
      from django.db import models

      # Create your models here.

      # Airport
      class Airport(models.Model):
        code = models.CharField(max_length=3)
        city = models.CharField(max_length=60)

        # Turn data returned to formatted string
        def __str__(self) -> str:
          return f'{ self.city } ({ self.code })'


      # Flight
      class Flight(models.Model):
        # Reference Airport table w/ FK deletes if Airport deletes
        origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure')
        destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
        duration = models.IntegerField()

        # Turn data returned to formatted string
        def __str__(self) -> str:
          return f'{ self.id }: { self.origin } to { self.destination }'

      # Passenger
      class Passenger(models.Model):
        first = models.CharField(max_length=30)
        last = models.CharField(max_length=30)
        # Create a ManyToMany relationship w/ Flight
        flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')
        
        # Turn data returned to formatted string
        def __str__(self) -> str:
          return f'{ self.first } { self.last }'
    ```

  

## Database

  ### Makemigrations
  Gives database access to models
  - `py manage.py makemigrations`
    ```
      Migrations for 'flights':
        flights\migrations\0001_initial.py
          - Create model Flight
    ```

    After modifying models makemigrations again
      ```
        Migrations for 'flights':
          flights\migrations\0002_airport_alter_flight_destination_alter_flight_origin.py
            - Create model Airport
            - Alter field destination on flight
            - Alter field origin on flight
      ```
    
    After modifying models makemigrations again
      ```
        Migrations for 'flights':
          flights\migrations\0003_passenger.py
            - Create model Passenger
      ```

  ### Migrate
  Migrates models to database
  - `py manage.py migrate`
    ```
      Operations to perform:
        Apply all migrations: admin, auth, contenttypes, flights, sessions   
      Running migrations:
        Applying contenttypes.0001_initial... OK
        Applying auth.0001_initial... OK
        Applying admin.0001_initial... OK
        Applying ... OK
        Applying ... OK
        Applying flights.0001_initial... OK
        Applying sessions.0001_initial... OK
    ```

    After modifying models migrate again
    ```
      Operations to perform:
        Apply all migrations: admin, auth, contenttypes, flights, sessions    
      Running migrations:
        Applying flights.0002_airport_alter_flight_destination_alter_flight_origin... OK
    ```
    
    After modifying models migrate again
    ```
      Operations to perform:
        Apply all migrations: admin, auth, contenttypes, flights, sessions
      Running migrations:
        Applying flights.0003_passenger... OK
    ```



## Shell

  ### Manipulate Database Data
  - `py manage.py shell`
    ```
      #Import Flight model
      In [1]: from flights.models import Flight

      #Create a Flight
      In [2]: f = Flight(origin="New York", destination="London", duration=415)

      #Save flight
      In [3]: f.save()

      #Query a flight
      In [4]: Flight.objects.all()
      Out[4]: <QuerySet [<Flight: Flight object (1)>]>

      #Update model to stringify data and restart shell
      In [1]: from flights.models import Flight

      In [2]: flights = Flight.objects.all()

      In [3]: flights
      Out[3]: <QuerySet [<Flight: 1: New York to London>]>

      #Get the first object
      In [4]: flight = flights.first()

      In [5]: flight
      Out[5]: <Flight: 1: New York to London>

      #Query flight id, origin, destination, duration
      In [6]: flight.id
      Out[6]: 1

      In [7]: flight.origin
      Out[7]: 'New York'

      In [8]: flight.destination
      Out[8]: 'London'

      In [9]: flight.duration
      Out[9]: 415

      #Delete flight
      In [10]: flight.delete()
      Out[10]: (1, {'flights.Flight': 1})

      #Import all models for manipulation
      In [1]: from flights.models import *

      #Create Airport(s)
      In [2]: jfk = Airport(code="JFK", city="New York")
      #Save airport
      In [3]: jfk.save()

      In [4]: lhr = Airport(code="LHR", city="London")
      #Save airport
      In [5]: lhr.save()

      In [6]: cdg = Airport(code="CDG", city="Paris")
      #Save airport
      In [7]: cdg.save()

      In [8]: nrt = Airport(code="NRT", city="Tokyo")
      #Save airport
      In [9]: nrt.save()

      #Create Flight(s)
      In [10]: f = Flight(origin=jfk, destination=lhr, duration=415)
      #Save flight
      In [11]: f.save()

      #Call flight instance
      In [12]: f
      Out[12]: <Flight: 1: New York (JFK) to London (LHR)>

      #Query flight origin, origin city, origin code
      In [13]: f.origin
      Out[13]: <Airport: New York (JFK)>

      In [14]: f.origin.city
      Out[14]: 'New York'

      In [15]: f.origin.code
      Out[15]: 'JFK'

      #Query flights arriving in London
      In [16]: lhr.arrivals.all()
      Out[16]: <QuerySet [<Flight: 1: New York (JFK) to London (LHR)>]>

      #Query all Airport(s)
      In [17]: Airport.objects.all()
      Out[17]: <QuerySet [<Airport: New York (JFK)>, <Airport: London (LHR)>, <Airport: Paris (CDG)>, <Airport: Tokyo (NRT)>]>

      #Filter Airport query where the city is New York
      In [18]: Airport.objects.filter(city="New York")
      Out[18]: <QuerySet [<Airport: New York (JFK)>]>

      #Get the first instance of Airport where the city is New York
      In [19]: Airport.objects.filter(city="New York").first()
      Out[19]: <Airport: New York (JFK)>

      #If there is only one instance of Airport where the city is New York use .get() method
      In [20]: Airport.objects.get(city="New York")
      Out[20]: <Airport: New York (JFK)>

      #Create instance(s) of Airport(s)
      In [21]: jfk = Airport.objects.get(city="New York")

      In [22]: jfk
      Out[22]: <Airport: New York (JFK)>

      In [23]: cdg = Airport.objects.get(city="Paris")

      In [24]: cdg
      Out[24]: <Airport: Paris (CDG)>

      #Create a Flight from jfk/New York to cdg/Paris
      In [25]: f = Flight(origin=jfk, destination=cdg, duration=435)
      #Save flight
      In [26]: f.save()

      #





    ```

## Utilize Django built-in admin panel

  ### Create a Admin User account
  - `py manage.py createsuperuser`
    ```
      Username (leave blank to use 'xxxx'): username
      Email address: local-part@domain.com
      Password: 
      Password (again): 
      This password is too short. It must contain at least 8 characters.
      This password is too common.
      This password is entirely numeric.
      Bypass password validation and create user anyway? [y/N]: 
      Superuser created successfully.
    ```

  ### Register models for use in admin database
  - project_name/app_name/admin.py
    ```
      from django.contrib import admin

      # Register your models here.
      from .models import Flight, Airport, Passenger

      # View Flight in Admin Panel as informed list
      class FlightAdmin(admin.ModelAdmin):
        list_display = ('id', 'origin', 'destination', 'duration')

      # View Passenger in Admin Panel with the option to filter flight the passenger is on and available flights
      class PassengerAdmin(admin.ModelAdmin):
        filter_horizontal = ('flights',)

      admin.site.register(Airport)
      admin.site.register(Flight, FlightAdmin)
      admin.site.register(Passenger, PassengerAdmin)
    ```

## Views

  ### Create a view: 
  - Flights App

  - app_name/views.py
    ```
      #Create index view that renders all flights to index template:
      from django.shortcuts import render
      from django.http import HttpResponse
      from .models import Flight, Passenger
      from django.urls import reverse

      # Create your views here.

      # index view:Show all available flight
      def index(request):
        return render(request, 'flights/index.html', {
          'flights': Flight.objects.all()
        })

      #Create a flight view that renders flight based on the pk to flight template

      #Flight
      def flight(request, flight_id):
        flight = Flight.objects.get(pk=flight_id)
        return render(request, 'flights/flight.html', {
          'flight': flight
        })

      #Create a book view that renders a booked flight based on the pk and form request to flight template
      def book(request, flight_id):
        if request.method == 'POST':
          flight = Flight.objects.get(pk=flight_id)
          passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
          passenger.flights.add(flight)
          return HttpResponseRedirect(reverse('flight', args=(flight.id,)))
    ``` 

  ### Create app views
  - Users App
  
  - app_name/views.py
  ```
    #Create a index view that checks if users is authenticated, if not redirect to login page
  ```


## Templates

  ### Create templates file structure
  - project_name/app_name/templates
    *Within the **templates** directory create another folder with the same name as app_name directory*

  - templates/app_name
    *Create template file*

  - templates/app_name/layout.html
  Layout file will be the base structure html files follow
    ```
      <!DOCTYPE html>
      <html lang="en">
      <head>
        <title>Flights</title>
      </head>
      <body>
        {% block body %}
        
        {% endblock %}
      </body>
      </html>
    ```
  
  - templates/app_name/index.html
  Create index file that extends layout.html and loops through Flights variable and displays flight id, origin and destination in a ul
    ```
      {% extends 'flights/layout.html' %}

      {% block body %}
        <h1>Flights</h1>
        <ul>
          {% for flight in flights %}
            #Turn each li into that renders associated flight page by flight id
            <li>
              <a href="{% url 'flight' flight.id %}">Flight {{ flight.id }}: {{ flight.origin }} to {{ flight.destination }}</a>
            </li>
          {% endfor %}
        </ul>

      {% endblock %}
    ```
  
  - templates/app_name/flight.html
  Create flight file that extends layout.html and displays flight id heading, origin and destination in a list
    ```
      {% extends 'flights/layout.html' %}

      {% block body %}
        <h1>Flight {{ flight.id }}</h1>
        <ul>
          <li>Origin: {{ flight.origin }}</li>
          <li>Destination: {{ flight.destination }}</li>
          <li>Duration: {{ flight.duration }}</li>
        </ul>

        #Loop through passengers and display passengers on flight in a list otherwise show message
        <h2>Passengers</h2>
        <ul>
          {% for passenger in passengers %}
            <li>{{ passenger }}</li>
          {% empty %}
            <li>No passengers.</li>
          {% endfor %}
        </ul>

        #Add a form that submit a booked passenger from a list of options
        <h2>Add Passenger</h2>
        <form action="{% url 'book' flight.id %}" method="post">
          {% csrf_token %}
          <select name="passenger">
            {% for passenger in non_passengers %}
              <option value="{{ passenger.id }}">{{ passenger }}</option>
            {% endfor %}
          </select>
          <input type="submit">
        </form>

        #Link back to flight list
        <a href="{% url 'index' %}">Back to  Flight List</a>
      {% endblock %}
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