# Generated by Django 3.1.6 on 2021-03-23 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0007_auto_20210323_1721'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='mptt_level',
            new_name='level',
        ),
    ]
