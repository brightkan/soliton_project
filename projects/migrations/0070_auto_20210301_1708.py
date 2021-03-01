# Generated by Django 2.2.2 on 2021-03-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0069_merge_20210301_1636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='role',
        ),
        migrations.AddField(
            model_name='worker',
            name='profile',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='worker',
            name='type',
            field=models.CharField(choices=[('ISP', 'ISP'), ('OFC', 'OFC'), ('Financial', 'Financial'), ('Warehouse', 'Warehouse'), ('Power', 'Power'), ('Maintenance', 'Maintenance'), ('Workshop', 'Workshop'), ('Administrator', 'Administrator')], default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='worker',
            name='business_unit',
            field=models.CharField(choices=[('MS', 'Managed Services'), ('CN', 'Connectivity'), ('ND', 'Network Deployment'), ('QL', 'Quality'), ('ET', 'Emerging Technologies'), ('SU', 'Support')], max_length=2),
        ),
        migrations.AlterField(
            model_name='worker',
            name='national_id',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='worker',
            name='national_id_document',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AlterField(
            model_name='worker',
            name='next_of_kin',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
