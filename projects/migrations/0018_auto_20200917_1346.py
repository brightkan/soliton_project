# Generated by Django 2.2.2 on 2020-09-17 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_executionscope'),
    ]

    operations = [
        migrations.AlterField(
            model_name='executionscope',
            name='survey',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.Survey'),
        ),
    ]
