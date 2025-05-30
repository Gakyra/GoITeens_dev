# Generated by Django 5.1.5 on 2025-03-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stuff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuff_id', models.CharField(max_length=100)),
                ('stuff_name', models.CharField(max_length=255)),
                ('stuff_desc', models.TextField()),
                ('photo', models.ImageField(upload_to='stuff_photos/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
