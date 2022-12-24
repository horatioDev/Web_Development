from django.shortcuts import render

# Import Flight
from .models import Flight, Passenger

# Import for HttpResponseRedirect redirection 
from django.http import HttpResponseRedirect

# Import reverse to template
from django.urls import reverse

# Create your views here.
def index(request):
  return render(request, 'flights/index.html', {
    'flights': Flight.objects.all()
  })

# Flight 
def flight(request, flight_id):
  flight = Flight.objects.get(pk=flight_id)
  return render(request, 'flights/flight.html', {
    'flight': flight,
    'passengers': flight.passengers.all(),
    'non_passengers': Passenger.objects.exclude(flights=flight).all()
  })

# Book a Flight
def book(request, flight_id):
  if request.method == 'POST':
    flight = Flight.objects.get(pk=flight_id)
    passenger = Passenger.objects.get(pk=int(request.POST['passenger']))
    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flight', args=(flight.id,)))