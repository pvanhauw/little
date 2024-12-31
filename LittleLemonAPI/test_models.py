from django.test import TestCase
from .models import MenuItem

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


