# Generated by Django 3.2.15 on 2022-10-16 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='index',
            name='cpass',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='index',
            name='passw',
            field=models.CharField(max_length=20),
        ),
    ]