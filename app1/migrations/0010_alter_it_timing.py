# Generated by Django 4.1.2 on 2022-11-06 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_alter_it_timing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='it',
            name='timing',
            field=models.DateTimeField(),
        ),
    ]
