# Generated by Django 2.2.1 on 2021-02-11 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0063_auto_20210211_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='wagesheet',
            name='wage_bill',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.WageBill'),
        ),
    ]