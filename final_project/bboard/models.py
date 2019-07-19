from django.db import models
from django.urls import reverse


class Advertisement (models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default="user")
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('adv_detail', args=[str(self.id)])
