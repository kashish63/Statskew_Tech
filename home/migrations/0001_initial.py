# Generated by Django 3.2.15 on 2022-10-14 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('passw', models.TextField()),
                ('cpass', models.TextField()),
            ],
        ),
    ]
