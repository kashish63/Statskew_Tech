# Generated by Django 3.2.15 on 2022-12-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20221207_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='handledatascience',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='handledatascience',
            name='email',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='handledatascience',
            name='gender',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='handledatascience',
            name='lastname',
            field=models.CharField(max_length=122, null=True),
        ),
        migrations.AddField(
            model_name='handledatascience',
            name='phone',
            field=models.CharField(max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='handledatascience',
            name='firstname',
            field=models.CharField(max_length=122, null=True),
        ),
    ]
