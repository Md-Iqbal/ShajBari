# Generated by Django 3.1.7 on 2021-04-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_order', '0016_auto_20210406_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='transactionId',
            field=models.CharField(blank=True, editable=False, max_length=255, null=True),
        ),
    ]