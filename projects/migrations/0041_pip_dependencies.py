# Generated by Django 2.2.1 on 2020-10-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0040_merge_20201019_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='pip',
            name='dependencies',
            field=models.ManyToManyField(related_name='dependencies', to='projects.Activity'),
        ),
    ]
