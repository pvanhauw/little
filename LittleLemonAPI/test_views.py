from django.test import TestCase, Client
from django.urls import reverse
from .models import MenuItem
from .serializers import MenuItemSerializer
class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item2 = MenuItem.objects.create(title="Pizza", price=120, inventory=50)

    def test_getall(self):
        url = reverse('menu-items')  # Assuming you have named your URL pattern 'menu-items'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.data, serializer.data)
        
    def test_getall_menu_objects(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
        # Verify the number of menu items
        self.assertEqual(MenuItem.objects.count(), 2)
        
        # Verify the details of menu items
        menu_items = MenuItem.objects.all()
        self.assertEqual(menu_items[0].title, "IceCream")
        self.assertEqual(menu_items[0].price, 80)
        self.assertEqual(menu_items[0].inventory, 100)
        self.assertEqual(menu_items[1].title, "Pizza") 
        self.assertEqual(menu_items[1].price, 120)
        self.assertEqual(menu_items[1].inventory, 50)
        
    def test_post(self):
        url = reverse('menu-items')
        data = {
            "title": "Burger",
            "price": 150,
            "inventory": 75
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(MenuItem.objects.count(), 3)
        self.assertEqual(MenuItem.objects.get(title="Burger").price, 150)
        
    def test_get_single_item(self):
        response = self.client.get(f'/api/menu-items/{self.menu_item1.id}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], self.menu_item1.title)
        
    def test_update_item(self):
        data = {
            "title": "Vanilla IceCream",
            "price": 85,
            "inventory": 90
        }
        response = self.client.put(f'/api/menu-items/{self.menu_item1.id}', data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.menu_item1.refresh_from_db()
        self.assertEqual(self.menu_item1.title, "Vanilla IceCream")
        self.assertEqual(self.menu_item1.price, 85)
        
    def test_delete_item(self):
        response = self.client.delete(f'/api/menu-items/{self.menu_item1.id}')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(MenuItem.objects.count(), 1)
