# Generated by Django 2.2.2 on 2020-09-16 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20200916_0853'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='serviceboqitem',
            unique_together={('boq', 'activity')},
        ),
    ]