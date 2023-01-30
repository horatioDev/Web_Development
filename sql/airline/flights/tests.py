# Import Max model
from django.db.models import Max

# Import Client, and Test
from django.test import Client, TestCase

# Import Models used in TestCase
from .models import Airport, Flight, Passenger

# Create your tests here.
"""Run tests in terminal: py manage.py test"""
class FlightTestCase(TestCase):
  # Setup is the testing framework method that will automatically call for every single test we run. Creating a dummy data testing database separate from original
  def setUp(self):

    # Create airport(s) to test
    a1 = Airport.objects.create(code="AAA", city="City A")
    a2 = Airport.objects.create(code="BBB", city="City B")

    # Create flight(s) to test
    # Valid Flight
    Flight.objects.create(origin=a1, destination=a2, duration=100)

    # Invalid Flight(s)
    Flight.objects.create(origin=a1, destination=a1, duration=200)
    Flight.objects.create(origin=a1, destination=a2, duration=-100)

  # Test the amount of departure(s)
  def test_departures_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.departures.count(), 3)
  
  # Test the amount of arrival(s)
  def test_arrivals_count(self):
    a = Airport.objects.get(code="AAA")
    self.assertEqual(a.arrivals.count(), 1)

  # Test is valid flight
  def test_valid_flight(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code="BBB")
    f = Flight.objects.get(origin=a1, destination=a2, duration=100)
    self.assertTrue(f.is_valid_flight())
  
  # Test is invalid flight destination
  def test_invalid_flight_destination(self):
    a1 = Airport.objects.get(code="AAA")
    f = Flight.objects.get(origin=a1, destination=a1)
    self.assertFalse(f.is_valid_flight())
  
  # Test is invalid flight duration
  def test_invalid_flight_duration(self):
    a1 = Airport.objects.get(code="AAA")
    a2 = Airport.objects.get(code="BBB")
    f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
    self.assertFalse(f.is_valid_flight())

  # Test flight(s) default page index
  def test_index(self):
    # Create a Client object
    c = Client()
    # Get Client flights
    response = c.get("/flights/")

    # Assert status code = 200
    # Assert count = 3
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["flights"].count(), 3)

  # Test if valid flight page
  def test_valid_flight_page(self):
    a1 = Airport.objects.get(code="AAA")
    f = Flight.objects.get(origin=a1, destination=a1)
    c =Client()
    # Get client flight by id
    response= c.get(f"/flights/{f.id}")

    # Assert status code = 200
    self.assertEqual(response.status_code, 200)
  
  # Test if invalid flight page
  def test_invalid_flight_page(self):
    # Get the largest id from the flights
    max_id = Flight.objects.all().aggregate(Max("id"))["id__max"]
    c = Client()
    response = c.get(f"/{max_id + 1}")    

    # Assert status code = 404
    self.assertEqual(response.status_code, 404)
    

  # Test flight page passengers
  def test_flight_page_passengers(self):
    f = Flight.objects.get(pk=1)
    p = Passenger.objects.create(first="Ray", last="Xavier")

    # Add passenger to flight
    f.passengers.add(p)
    c = Client()
    response = c.get(f"/flights/{f.id}")

    # Assert status code = 200
    # Assert passenger count = 1
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["passengers"].count(), 1)
  
  # Test flight page non-passengers
  def test_flight_page_non_passengers(self):
    f = Flight.objects.get(pk=1)
    p = Passenger.objects.create(first="Xavier", last="Hanley")

    c = Client()
    response = c.get(f"/flights/{f.id}")

    # Assert status code = 200
    # Assert passenger count = 1
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.context["non_passengers"].count(), 1)


"""
Output:
  Found 5 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  .EFF.
  ======================================================================
  ERROR: test_departures_count (flights.tests.FlightTestCase)

  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\airline\flights\tests.py", line 34, in test_departures_count
      self.assertEqual(a.departures.count(), 3)
  AttributeError: 'Airport' object has no attribute 'departures'

  ======================================================================
  FAIL: test_invalid_flight_destination (flights.tests.FlightTestCase)
  ----------------------------------------------------------------------
  Traceback (most recent call last):
    File "C:\airline\flights\tests.py", line 52, in test_invalid_flight_destination    
      self.assertFalse(f.is_valid_flight())
  AssertionError: True is not false

  ======================================================================
  FAIL: test_invalid_flight_duration (flights.tests.FlightTestCase)
  -----------Ran 5 tests in 0.076s

  FAILED (failures=2, errors=1)Destroying test database for alias 'default'...

Update Output:
  Found 10 test(s).
  Creating test database for alias 'default'...
  System check identified no issues (0 silenced).
  ..........
  ----------------------------------------------------------------------
  Ran 10 tests in 0.142s

  OK
  Destroying test database for alias 'default'...

"""