# Generated by Django 4.1.2 on 2022-11-06 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_alter_items_data_current_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_data',
            name='Current_Time',
            field=models.DateTimeField(default='2022-11-06 20:01:48 IST+0530'),
        ),
    ]
