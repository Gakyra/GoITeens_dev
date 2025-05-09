from django.db import models
from django.contrib.auth.models import User


class Stuff(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.PositiveIntegerField()
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
