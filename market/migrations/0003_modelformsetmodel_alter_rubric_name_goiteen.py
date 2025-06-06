# Generated by Django 5.1.5 on 2025-03-03 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_bb_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelFormsetModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('department', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='rubric',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='GoITeen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.rubric')),
            ],
        ),
    ]
