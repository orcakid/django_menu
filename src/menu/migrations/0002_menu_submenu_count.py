# Generated by Django 4.1.7 on 2023-03-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='submenu_count',
            field=models.IntegerField(default=0),
        ),
    ]
