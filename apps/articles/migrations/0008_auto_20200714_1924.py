# Generated by Django 3.0.7 on 2020-07-14 14:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20200712_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Category',
            field=models.CharField(blank=True, choices=[('3D', '3D'), ('Photo', 'Фотография'), ('Portrait', 'Портрет'), ('Art', 'Арт'), ('Landscape', 'Пейзаж')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='DateAdded',
            field=models.DateField(default=datetime.date(2020, 7, 14)),
        ),
        migrations.AlterField(
            model_name='article',
            name='DateTimeAdded',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='article_comment',
            name='DateAdded',
            field=models.DateField(default=datetime.date(2020, 7, 14)),
        ),
        migrations.AlterField(
            model_name='article_comment',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 14, 14, 24, 25, 436336, tzinfo=utc)),
        ),
    ]