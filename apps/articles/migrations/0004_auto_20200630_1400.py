# Generated by Django 3.0.7 on 2020-06-30 09:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200629_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='DateAdded',
            field=models.DateField(default=datetime.date(2020, 6, 30)),
        ),
        migrations.AlterField(
            model_name='article',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 9, 0, 48, 623487, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article_comment',
            name='DateAdded',
            field=models.DateField(default=datetime.date(2020, 6, 30)),
        ),
        migrations.AlterField(
            model_name='article_comment',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 9, 0, 48, 622487, tzinfo=utc)),
        ),
    ]
