from django.test import TestCase
from .models import Inventory
from django.db import IntegrityError

class InventoryModelTest(TestCase):
    def setUp(self):
        # Create an initial inventory item
        self.item = Inventory.objects.create(name='Tomatoes', quantity=50)
    
    def test_inventory_creation(self):
        """Test that inventory item is created correctly."""
        item = Inventory.objects.get(name='Tomatoes')
        self.assertEqual(item.name, 'Tomatoes')
        self.assertEqual(item.quantity, 50)
        self.assertIsNotNone(item.timestamp)  # auto_now=True should set this

    def test_inventory_str(self):
        """Test the __str__ method outputs expected format."""
        item = Inventory.objects.get(name='Tomatoes')
        expected_str = f"{item.name}: {item.quantity} - {item.timestamp}"
        self.assertEqual(str(item), expected_str)
    
    def test_inventory_unique_name(self):
        """Test that the name field is unique and raises IntegrityError if duplicated."""
        with self.assertRaises(IntegrityError):
            Inventory.objects.create(name='Tomatoes', quantity=30)
    
    def test_inventory_quantity_field(self):
        """Test that quantity field accepts expected values."""
        item = Inventory.objects.create(name='Potatoes', quantity=99)
        self.assertEqual(item.quantity, 99)
