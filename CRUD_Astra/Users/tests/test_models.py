from django.test import TestCase
from Users.models import User
# Create your tests here.

class TestModelUser(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(name='Daniel Test', mail='mail@test.com')
    
    def test_name_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_mail_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('mail').verbose_name
        self.assertEqual(field_label, 'mail')

    def test_date_of_creation(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('date').verbose_name
        self.assertEqual(field_label, 'date')

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('name').max_length
        self.assertEqual(max_length, 100)

    def test_name_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('mail').max_length
        self.assertEqual(max_length, 100)


    