# Generated by Django 4.1.2 on 2022-11-06 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_alter_items_data_current_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='items_data',
            name='Top_Bidder',
            field=models.CharField(max_length=30, null=True),
        ),
    ]