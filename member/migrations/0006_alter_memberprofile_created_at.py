# Generated by Django 3.2.9 on 2021-12-11 20:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_alter_memberprofile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberprofile',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 11, 20, 24, 50, 185185, tzinfo=utc)),
        ),
    ]
