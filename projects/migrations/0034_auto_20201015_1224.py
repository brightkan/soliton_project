# Generated by Django 2.2.2 on 2020-10-15 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0033_auto_20201015_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pipteam',
            old_name='date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='pipteam',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]