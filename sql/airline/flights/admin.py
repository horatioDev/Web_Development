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