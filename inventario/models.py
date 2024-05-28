from django.db import models

class Reservation(models.Model):
    name = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=20, default='')
    email = models.EmailField(max_length=254, default='')
    
    def __str__(self):
        return f'Reservación para {self.name} ({self.email})'

