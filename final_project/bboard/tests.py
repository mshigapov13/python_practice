from django.test import TestCase

from .models import Advertisement

class AdvertisementModelTest(TestCase):
    def setUp(self):
        Advertisement.objects.create(text='just a test')
    
    def test_text_content(self):
        advertisement = Advertisement.objects.get(id=1)
        expected_obj_name = f'{advertisement.text}'
        self.assertEqual(expected_obj_name, 'just a test')
