from django.db import models

class Stuff(models.Model):
    stuff_id = models.CharField(max_length=100)
    stuff_name = models.CharField(max_length=255)
    stuff_desc = models.TextField()
    photo = models.ImageField(upload_to='stuff_photos/')
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.stuff_name
