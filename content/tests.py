from django.test import TestCase
from django.urls import reverse
from .models import DailyMailColumn
import datetime

class DailyMailColumnModelTest(TestCase):

    def setUp(self):
        self.column = DailyMailColumn.objects.create(
            link='https://www.test.com',
            title='test title',
            columnist='test columnist'
        )

    def test_string_representation(self):
        self.assertEqual(str(self.column), self.column.title)

    def test_column_content(self):
        self.assertEqual(f'{self.column.link}', 'https://www.test.com')
        self.assertEqual(f'{self.column.title}', 'test title')
        self.assertEqual(f'{self.column.columnist}', 'test columnist')
        self.assertTrue(isinstance(self.column.date_added, datetime.datetime))

    def test_columns_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'test title')

class HomePageViewTest(TestCase):

    def test_view_url_exists_at_proper_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')