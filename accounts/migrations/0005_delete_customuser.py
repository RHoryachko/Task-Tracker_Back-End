# Generated by Django 3.2.23 on 2023-12-11 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_emailverification_verification_token'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
