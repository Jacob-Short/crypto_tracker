# Generated by Django 3.2.9 on 2021-12-10 21:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_favoritecrypto_date_added_as_fav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favoritecrypto',
            name='date_added_as_fav',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 10, 21, 5, 13, 161782, tzinfo=utc)),
        ),
    ]
