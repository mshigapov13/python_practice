from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Advertisement


class AdvertisementTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )

        self.advertisement = Advertisement.objects.create(
            title='Test title',
            body='Test body',
            author=self.user,
        )
    
    def test_string_representation(self):
        advertisement = Advertisement(title='Sample title')
        self.assertEqual(str(advertisement), advertisement.title)

    def test_adv_detail_view(self):
        response = self.client.get('/adv/1/')
        no_response = self.client.get('/adv/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Test title')
        self.assertTemplateUsed(response, 'adv_detail.html')

    def test_adv_list_view(self):
        response = self.client.get(reverse('advs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test body')
        self.assertTemplateUsed(response, 'advs.html')

    def test_adv_content(self):
        self.assertEqual(f'{self.advertisement.title}', 'Test title')
        self.assertEqual(f'{self.advertisement.author}', 'testuser')
        self.assertEqual(f'{self.advertisement.body}', 'Test body')
    
    def test_adv_create_view(self):
        response = self.client.post(reverse('adv_new'), {
            'title': 'New Test title',
            'body': 'New Test text',
            'author': self.user,
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'New Test title')
        self.assertContains(response, 'New Test text')

    def test_adv_update_view(self):
        response = self.client.post(reverse('adv_edit', args='1'),
        {'title': 'Updated title', 'body': 'Updated body'})
        self.assertEqual(response.status_code, 302)

    def test_adv_delete_view(self):
        response = self.client.get(
            reverse('adv_delete', args='1')
        )
        self.assertEqual(response.status_code, 200)
