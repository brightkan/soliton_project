# Generated by Django 2.2.2 on 2020-10-15 12:07

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_pipteam'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pipteam',
            name='date',
        ),
        migrations.AddField(
            model_name='pipteam',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pipteam',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 15, 12, 7, 37, 853909, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ActivityTeamAssignment',
        ),
    ]
