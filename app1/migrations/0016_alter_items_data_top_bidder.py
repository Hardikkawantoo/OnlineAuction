# Generated by Django 4.1.2 on 2022-11-06 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_items_data_top_bidder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items_data',
            name='Top_Bidder',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
