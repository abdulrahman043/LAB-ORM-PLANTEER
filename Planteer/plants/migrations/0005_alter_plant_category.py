# Generated by Django 5.1.7 on 2025-03-10 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='category',
            field=models.CharField(choices=[('Vegetable', 'Vegetable'), ('Fruit', 'Fruit'), ('Tree', 'Tree')], max_length=1024),
        ),
    ]
