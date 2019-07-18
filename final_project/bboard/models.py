from django.db import models

class Advertisement (models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]