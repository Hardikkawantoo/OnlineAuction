# Generated by Django 4.1.2 on 2022-11-01 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_data',
            name='Timing',
            field=models.DateTimeField(),
        ),
    ]
