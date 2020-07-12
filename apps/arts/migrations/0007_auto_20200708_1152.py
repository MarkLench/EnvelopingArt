# Generated by Django 3.0.7 on 2020-07-08 06:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('arts', '0006_auto_20200630_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art',
            name='DateAdded',
            field=models.DateField(default=datetime.date(2020, 7, 8)),
        ),
        migrations.AlterField(
            model_name='art',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 6, 52, 19, 210620, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='art_comment',
            name='DateAdded',
            field=models.DateField(default=datetime.date(2020, 7, 8)),
        ),
        migrations.AlterField(
            model_name='art_comment',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 8, 6, 52, 19, 209119, tzinfo=utc)),
        ),
    ]
