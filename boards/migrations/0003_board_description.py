# Generated by Django 3.2.23 on 2023-12-20 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0002_board'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
