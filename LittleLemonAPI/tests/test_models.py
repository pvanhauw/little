from django.test import TestCase
from LittleLemonAPI.models import MenuItem, Booking
from datetime import datetime
class MenuItemTest(TestCase):
    def setUp(self):
        self.item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    
    def test_get_item(self):
        itemstr = self.item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")

    def test_get_item2(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        itemstr = item.get_item()
        self.assertEqual(itemstr, "IceCream : 80")

    def test_item_title(self):
        self.assertEqual(self.item.title, "IceCream")
    
    def test_item_price(self):
        self.assertEqual(self.item.price, 80)

class BookingTest(TestCase):
    def setUp(self):
        self.test_date = datetime(2024, 1, 1, 10, 30, 0)
        self.booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=2,
            booking_date=self.test_date
        )
    
    def test_booking_name(self):
        self.assertEqual(self.booking.name, "John Doe")
    
    def test_booking_no_of_guests(self):
        self.assertEqual(self.booking.no_of_guests, 2)
    
    def test_booking_date(self):
        self.assertEqual(self.booking.booking_date, self.test_date)
