# Generated by Django 4.2.6 on 2023-10-13 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='products_cart',
        ),
    ]