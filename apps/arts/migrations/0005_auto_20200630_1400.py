# Generated by Django 3.0.7 on 2020-06-30 09:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('arts', '0004_auto_20200629_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='art_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AdminComment', models.BooleanField(default=False)),
                ('Body', models.CharField(max_length=512)),
                ('Likes', models.PositiveIntegerField(default=0)),
                ('Dislikes', models.PositiveIntegerField(default=0)),
                ('DateAdded', models.DateField(default=datetime.date(2020, 6, 30))),
                ('DateTimeAdded', models.DateTimeField(default=datetime.datetime(2020, 6, 30, 9, 0, 48, 631489, tzinfo=utc))),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='art_comment_author', to=settings.AUTH_USER_MODEL)),
                ('Parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='child_set', to='arts.art_comment')),
            ],
        ),
        migrations.AlterField(
            model_name='art',
            name='DateAdded',
            field=models.DateField(default=datetime.date(2020, 6, 30)),
        ),
        migrations.AlterField(
            model_name='art',
            name='DateTimeAdded',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 30, 9, 0, 48, 632488, tzinfo=utc)),
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.AlterField(
            model_name='art',
            name='Comments',
            field=models.ManyToManyField(blank=True, null=True, to='arts.art_comment'),
        ),
    ]