# Generated by Django 2.2.2 on 2020-10-16 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0038_auto_20201016_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='mobile_money_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]