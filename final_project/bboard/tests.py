from django.test import TestCase
from django.urls import reverse

from .models import Advertisement

class AdvertisementModelTest(TestCase):
    def setUp(self):
        Advertisement.objects.create(text='just a test')
    
    def test_text_content(self):
        advertisement = Advertisement.objects.get(id=1)
        expected_obj_name = f'{advertisement.text}'
        self.assertEqual(expected_obj_name, 'just a test')

class AdvertisementsPageViewTest(TestCase):
    def setUp(self):
        Advertisement.objects.create(text='this is another test')
    
    def test_view_url_exists_at_proper_location(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)
    
    def test_view_url_by_name(self):
        resp = self.client.get(reverse('advs'))
        self.assertEqual(resp.status_code, 200)
    
    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('advs'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'advs.html')