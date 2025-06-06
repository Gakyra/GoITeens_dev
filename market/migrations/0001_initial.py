# Generated by Django 5.1.5 on 2025-02-10 17:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
            ],
        ),
        migrations.CreateModel(
            name='Bb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Назва')),
                ('content', models.TextField(verbose_name='Опис')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Фото')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.rubric', verbose_name='Рубрика')),
            ],
        ),
    ]
