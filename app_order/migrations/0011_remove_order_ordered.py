# Generated by Django 3.1.7 on 2021-04-06 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0010_remove_order_orderitems'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
    ]
