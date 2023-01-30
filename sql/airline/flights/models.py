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
  origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
  destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
  duration = models.IntegerField()

  # Turn data returned to formatted string
  def __str__(self) -> str:
    return f'{ self.id }: { self.origin } to { self.destination }'
     

  # Check if flight is valid
  def is_valid_flight(self):
    return self.origin != self.destination or self.duration > 0

# Passenger
class Passenger(models.Model):
  first = models.CharField(max_length=30)
  last = models.CharField(max_length=30)
  # Create a ManyToMany relationship w/ Flight
  flights = models.ManyToManyField(Flight, blank=True, related_name='passengers')
  
  # Turn data returned to formatted string
  def __str__(self) -> str:
    return f'{ self.first } { self.last }'