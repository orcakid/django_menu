# Generated by Django 4.1.7 on 2023-03-29 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menu_submenu_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('menus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
                ('submenus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.submenu')),
            ],
        ),
    ]
