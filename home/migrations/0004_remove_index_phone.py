# Generated by Django 3.2.15 on 2022-10-22 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='phone',
        ),
    ]
