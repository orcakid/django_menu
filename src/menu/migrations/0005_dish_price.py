# Generated by Django 4.1.7 on 2023-03-29 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_submenu_dish_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='dish',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
