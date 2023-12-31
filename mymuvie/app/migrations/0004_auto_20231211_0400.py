# Generated by Django 3.2.23 on 2023-12-11 04:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_movie_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watched',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='movie',
            name='added_on',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 11, 4, 0, 15, 488999, tzinfo=utc), verbose_name='date added'),
        ),
    ]
