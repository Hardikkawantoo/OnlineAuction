# Generated by Django 4.1.2 on 2022-11-01 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('i_name', models.CharField(max_length=30)),
                ('cost', models.CharField(max_length=30)),
                ('upload', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('Timing', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
