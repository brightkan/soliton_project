# Generated by Django 2.2.1 on 2021-02-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0057_auto_20210205_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='is_manager_approved',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='deduction',
            name='is_manager_approved',
            field=models.BooleanField(default=True),
        ),
    ]