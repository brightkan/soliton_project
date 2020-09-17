# Generated by Django 2.2.1 on 2020-09-15 13:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_merge_20200908_1530'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('file_url', models.FileField(null=True, upload_to='files')),
                ('title', models.CharField(max_length=50, null=True)),
                ('surveyor', models.CharField(blank=True, max_length=50, null=True)),
                ('acceptStatus', models.BooleanField(default=False)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surveyresult_site', to='projects.Site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SurveyResultComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('comment', models.CharField(max_length=255)),
                ('readStatus', models.BooleanField(default=False)),
                ('surveyor', models.CharField(blank=True, max_length=50, null=True)),
                ('survey_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SurveyResult_survey_result', to='projects.SurveyResult')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('survey_date', models.DateField()),
                ('survey_type', models.CharField(choices=[('FD-UG', 'Fibre Underground'), ('FD-Aerial', 'Fibre Aerial'), ('Site', 'Site'), ('LAN', 'LAN'), ('Tower', 'Tower'), ('Equipment', 'Equipment')], max_length=50)),
                ('scope', models.IntegerField()),
                ('unit_of_measure', models.CharField(max_length=15)),
                ('coordinates_lat', models.CharField(max_length=20, null=True)),
                ('coordinates_long', models.CharField(max_length=20, null=True)),
                ('surveyor', models.CharField(blank=True, max_length=50, null=True)),
                ('is_checked', models.BooleanField(default=False)),
                ('checked_by', models.CharField(max_length=50)),
                ('is_approved', models.BooleanField(default=False)),
                ('approved_by', models.CharField(max_length=50)),
                ('is_client_approved', models.BooleanField(default=False)),
                ('status', models.CharField(max_length=20)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
