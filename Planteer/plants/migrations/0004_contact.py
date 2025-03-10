# Generated by Django 5.1.7 on 2025-03-10 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=1024)),
                ('last_name', models.CharField(max_length=1024)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
