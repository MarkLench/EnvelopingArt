# Generated by Django 3.0.7 on 2020-06-29 09:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0002_auto_20200629_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 9, 34, 49, 227004, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 29, 9, 34, 49, 226004, tzinfo=utc)),
        ),
    ]
