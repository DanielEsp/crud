from django.test import TestCase
from Shipments.models import Shipment
# Create your tests here.

class TestModelShipment(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Shipment.objects.create(owner='Daniel Test', status='PD')
    
    def test_owner_label(self):
        shipment = Shipment.objects.get(id=1)
        field_label = shipment._meta.get_field('owner').verbose_name
        self.assertEqual(field_label, 'owner')

    def test_status_label(self):
        shipment = Shipment.objects.get(id=1)
        field_label = shipment._meta.get_field('status').verbose_name
        self.assertEqual(field_label, 'status')

    def test_date_of_creation(self):
        shipment = Shipment.objects.get(id=1)
        field_label = shipment._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_owner_max_length(self):
        shipment = Shipment.objects.get(id=1)
        max_length = shipment._meta.get_field('owner').max_length
        self.assertEqual(max_length, 100)

    def test_status_max_length(self):
        shipment = Shipment.objects.get(id=1)
        max_length = shipment._meta.get_field('status').max_length
        self.assertEqual(max_length, 2)


    