from django.test import TestCase 
from restaurant.models import Menu
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json
from restaurant.serializers import menuSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.title, "IceCream")
        self.assertEqual(item.price, 80)

class MenuViewTest(APITestCase):
    def setUp(self):
        self.menu_item1 = Menu.objects.create(title = "Pizza", price = 12.99, inventory = 5)
        self.menu_item2 = Menu.objects.create(title = "Burger", price = 8.99, inventory = 10)
        
    def test_getall(self):
        url = reverse('menu_items') # takes a view name as an argument and returns the corresponding URL
        response = self.client.get(url) # sends a GET request to the URL returned by 'reverse' and stores the response in the 'response' variable
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        menu_items = Menu.objects.all() # gets a queryset of all 'Menu' objects from the database
        serializer = menuSerializer(menu_items, many = True) # serializes the queryset of 'Menu' objects into a JSON-like format
        self.assertEqual(response.data, serializer.data)
                