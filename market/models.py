
from django.db import models
from django.contrib.auth.models import User

class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Назва')
    content = models.TextField(verbose_name='Опис')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Ціна')
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name='Фото')
    rubric = models.ForeignKey('Rubric', on_delete=models.CASCADE, verbose_name='Рубрика')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GoITeen(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)

    def __str__(self):
        return self.title





class ModelFormsetModel(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    department = models.CharField(max_length=255)

    def __str__(self):
        return self.name








class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Користувач")
    product = models.ForeignKey('Bb', on_delete=models.CASCADE, verbose_name="Продукт")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кількість")

    def __str__(self):
        return f"Кошик {self.user.username}: {self.product.title} ({self.quantity})"