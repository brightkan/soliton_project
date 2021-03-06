# Generated by Django 3.1.7 on 2021-04-27 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0013_auto_20210427_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('first_name', 'last_name')},
        ),
    ]
