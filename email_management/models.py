from django.db import models

# Create your models here.
class Lead(models.Model):
    created = models.DateTimeField(auto_now_add=True, blank=True)
    upadated = models.DateTimeField(auto_now=True, blank=True)
    email = models.EmailField( max_length=254)
    subscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email