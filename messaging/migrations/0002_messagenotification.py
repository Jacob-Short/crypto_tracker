# Generated by Django 3.2.9 on 2021-12-11 20:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messaging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_new', models.BooleanField(default=True)),
                ('time_notified', models.DateTimeField(default=django.utils.timezone.now)),
                ('member_notified', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagenotification_member_notified', to=settings.AUTH_USER_MODEL)),
                ('message', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='messagenotification_message', to='messaging.message')),
            ],
        ),
    ]