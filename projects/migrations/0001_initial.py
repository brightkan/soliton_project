# Generated by Django 3.1.7 on 2021-03-10 15:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('clients', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('user_role', models.CharField(blank=True, choices=[('Supervisor', 'Supervisor'), ('Field Manager', 'Field Manager'), ('Finance Office', 'Finance Office'), ('Project Manager', 'Project Manager'), ('General Manager', 'General Manager')], max_length=50)),
                ('password', models.CharField(max_length=120)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=150)),
                ('unit_measure', models.CharField(blank=True, max_length=10, null=True)),
                ('is_fd_underground', models.BooleanField(blank=True, default=False, null=True)),
                ('is_fd_arial', models.BooleanField(blank=True, default=False, null=True)),
                ('is_site_connection', models.BooleanField(blank=True, default=False, null=True)),
                ('is_tower_construction', models.BooleanField(blank=True, default=False, null=True)),
                ('is_lan_installation', models.BooleanField(blank=True, default=False, null=True)),
                ('is_equipment_installation', models.BooleanField(blank=True, default=False, null=True)),
                ('is_manhole_installation', models.BooleanField(blank=True, default=False, null=True)),
                ('unit_cost', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Activity',
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_cost_material', models.IntegerField(default=0)),
                ('total_cost_execution', models.IntegerField(default=0)),
                ('total_cost_expense', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Budget',
                'verbose_name_plural': 'Budgets',
            },
        ),
        migrations.CreateModel(
            name='DuctSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duct_code', models.CharField(default='DC', max_length=15)),
                ('duct_type', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'DuctSystem',
                'verbose_name_plural': 'DuctSystems',
            },
        ),
        migrations.CreateModel(
            name='ExecutionScope',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense', models.CharField(max_length=50)),
                ('rate', models.IntegerField(default=0)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Expense',
                'verbose_name_plural': 'Expenses',
            },
        ),
        migrations.CreateModel(
            name='FieldManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('uom', models.CharField(max_length=20)),
                ('unit_cost', models.IntegerField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('UGX', 'UGX')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='PIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(max_length=50)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.activity')),
                ('dependencies', models.ManyToManyField(related_name='dependencies', to='projects.Activity')),
                ('scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.executionscope')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('project_code', models.CharField(max_length=10, verbose_name='Code')),
                ('name', models.CharField(max_length=50, verbose_name='Project Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('start_date', models.DateField(verbose_name='Start Date')),
                ('expected_end_date', models.DateField(verbose_name='Expected End Date')),
                ('status', models.CharField(blank=True, choices=[('started', 'Started'), ('on_going', 'On Going'), ('on_hold', 'On Hold'), ('success', 'Success'), ('canceled', 'Canceled')], default='Started', max_length=20, null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client', verbose_name='Client Company')),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=5)),
                ('project_type', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'ProjectType',
                'verbose_name_plural': 'ProjectTypes',
            },
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('execution_scope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.executionscope')),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('site_name', models.CharField(max_length=50, null=True)),
                ('is_deleted', models.BooleanField(default=False, null=True)),
                ('is_completed', models.BooleanField(default=False, null=True)),
                ('is_accessible', models.BooleanField(default=False, null=True)),
                ('is_surveyed', models.BooleanField(default=False, null=True)),
                ('is_accepted', models.BooleanField(default=False, null=True)),
                ('site_location', models.CharField(blank=True, max_length=150, null=True)),
                ('location_lat', models.CharField(max_length=20, null=True)),
                ('location_long', models.CharField(max_length=20, null=True)),
                ('start_date', models.DateField(null=True)),
                ('survey_date', models.DateField(null=True)),
                ('expected_end_date', models.DateField(null=True)),
                ('current_stage', models.IntegerField(default=0)),
                ('archivedStatus', models.BooleanField(default=False)),
                ('ackStatus', models.BooleanField(default=False)),
                ('ack_date', models.DateField(null=True)),
                ('survey_time', models.CharField(blank=True, max_length=255, null=True)),
                ('can_client_view_survey_reports', models.BooleanField(default=False)),
                ('email_remainder_sent', models.BooleanField(default=False)),
                ('site_contact_person', models.CharField(blank=True, max_length=150, null=True)),
                ('site_contact_phone_number', models.IntegerField(blank=True, null=True)),
                ('is_connected', models.BooleanField(default=False)),
                ('is_ready_for_connection', models.BooleanField(default=False)),
                ('is_connection_request_acknowledged', models.BooleanField(default=False)),
                ('site_connection_date', models.DateTimeField(blank=True, null=True)),
                ('number_of_fleet_on_site', models.IntegerField(blank=True, null=True)),
                ('number_of_members_on_site', models.IntegerField(blank=True, null=True)),
                ('site_image', models.FileField(blank=True, null=True, upload_to='sites/')),
                ('isp_works_complete', models.BooleanField(default=False, null=True)),
                ('osp_works_complete', models.BooleanField(default=False, null=True)),
                ('ofc_works_complete', models.BooleanField(default=False, null=True)),
                ('site_powering_complete', models.BooleanField(default=False, null=True)),
                ('original_trenching_distance', models.IntegerField(blank=True, null=True)),
                ('current_trenching_distance', models.IntegerField(blank=True, null=True)),
                ('site_drawing', models.FileField(blank=True, null=True, upload_to='drawing/')),
                ('site_address', models.TextField(blank=True, null=True)),
                ('site_usd_rate', models.IntegerField(blank=True, null=True)),
                ('site_type', models.CharField(blank=True, choices=[('single', 'Single'), ('dual', 'Dual'), ('shared', 'Shared')], max_length=150, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
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
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surveyresult_site', to='projects.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_of_measure', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WageBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(default='Current', max_length=50)),
            ],
            options={
                'verbose_name': 'WageBill',
                'verbose_name_plural': 'WageBills',
                'ordering': ['status'],
                'unique_together': {('start_date', 'end_date')},
            },
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('national_id', models.CharField(blank=True, max_length=20)),
                ('joining_date', models.DateField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('mobile_money_number', models.CharField(max_length=10, unique=True)),
                ('address', models.CharField(max_length=15)),
                ('next_of_kin', models.CharField(blank=True, max_length=15)),
                ('type', models.CharField(choices=[('ISP', 'ISP'), ('OFC', 'OFC'), ('Financial', 'Financial'), ('Warehouse', 'Warehouse'), ('Power', 'Power'), ('Maintenance', 'Maintenance'), ('Workshop', 'Workshop'), ('Administrator', 'Administrator')], max_length=20)),
                ('business_unit', models.CharField(choices=[('MS', 'Managed Services'), ('CN', 'Connectivity'), ('ND', 'Network Deployment'), ('QL', 'Quality'), ('ET', 'Emerging Technologies'), ('SU', 'Support')], max_length=2)),
                ('national_id_document', models.FileField(blank=True, upload_to='documents')),
                ('profile', models.FileField(blank=True, upload_to='documents')),
            ],
        ),
        migrations.CreateModel(
            name='WageSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('is_submitted', models.BooleanField(default=False)),
                ('manager_status', models.BooleanField(null=True)),
                ('manager_comment', models.TextField(default='-')),
                ('project_manager_status', models.BooleanField(null=True)),
                ('project_manager_comment', models.TextField(default='-')),
                ('gm_status', models.BooleanField(null=True)),
                ('gm_comment', models.TextField(default='-')),
                ('field_manager_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('segment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='projects.segment')),
                ('supervisor_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wage_sheet_supervisor', to=settings.AUTH_USER_MODEL)),
                ('wage_bill', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.wagebill')),
            ],
            options={
                'unique_together': {('supervisor_user', 'field_manager_user', 'date')},
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('field_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.fieldmanager')),
                ('supervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.worker')),
            ],
            options={
                'unique_together': {('name', 'field_manager', 'supervisor')},
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
                ('survey_result', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='SurveyResult_survey_result', to='projects.surveyresult')),
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
                ('segmate', models.CharField(blank=True, max_length=50, null=True)),
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
                ('client_approved', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SitePower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('material_used', models.CharField(blank=True, max_length=255, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('powering_successful', models.BooleanField(blank=True, null=True)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('comment', models.CharField(blank=True, max_length=255, null=True)),
                ('equipment_used', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SitePIP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('task', models.CharField(blank=True, max_length=255, null=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('image', models.FileField(upload_to='siteimages')),
                ('lat', models.DecimalField(blank=True, decimal_places=12, max_digits=12, null=True)),
                ('long', models.DecimalField(blank=True, decimal_places=12, max_digits=12, null=True)),
                ('status', models.CharField(choices=[('before', 'before'), ('after', 'after')], max_length=255)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SiteDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('file', models.FileField(upload_to='sitedocuments')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Siteboq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('material', models.CharField(blank=True, max_length=50, null=True)),
                ('actual_quantity', models.IntegerField(blank=True, null=True)),
                ('estimate_quantity', models.IntegerField(blank=True, null=True)),
                ('boq_type', models.CharField(max_length=50, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('site', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='siteboq_site', to='projects.site')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProjectWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('region', models.CharField(choices=[('central', 'Central'), ('northern', 'Northern'), ('southern', 'Southern'), ('western', 'Western'), ('eastern', 'Eastern')], max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('unit_measure', models.CharField(max_length=50)),
                ('client_segmate', models.CharField(blank=True, max_length=50, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
                ('work_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.projecttype')),
            ],
            options={
                'verbose_name': 'ProjectWorks',
                'verbose_name_plural': 'ProjectWorks',
            },
        ),
        migrations.CreateModel(
            name='MaterialBudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_cost', models.IntegerField()),
                ('total_cost', models.IntegerField(default=0)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.budget')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.material')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseBudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('rate', models.IntegerField()),
                ('total_cost', models.IntegerField(default=0)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.budget')),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.expense')),
            ],
            options={
                'verbose_name': 'ExpenseBudget',
                'verbose_name_plural': 'ExpenseBudgets',
            },
        ),
        migrations.AddField(
            model_name='executionscope',
            name='survey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.survey'),
        ),
        migrations.CreateModel(
            name='ExecutionBudget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('unit_cost', models.IntegerField()),
                ('total_cost', models.IntegerField(default=0)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.budget')),
            ],
            options={
                'verbose_name': 'ExecutionBudget',
                'verbose_name_plural': 'ExecutionBudgets',
            },
        ),
        migrations.AddField(
            model_name='budget',
            name='pip',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.pip'),
        ),
        migrations.CreateModel(
            name='BOQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('survey', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='projects.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Wage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('is_manager_approved', models.BooleanField(default=True)),
                ('is_pm_approved', models.BooleanField(null=True)),
                ('is_gm_approved', models.BooleanField(null=True)),
                ('is_payed', models.BooleanField(null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.activity')),
                ('wage_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.wagesheet')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.worker')),
            ],
            options={
                'unique_together': {('worker', 'activity')},
            },
        ),
        migrations.CreateModel(
            name='ServiceBOQItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.activity')),
                ('boq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.boq')),
            ],
            options={
                'unique_together': {('boq', 'activity')},
            },
        ),
        migrations.CreateModel(
            name='PIPTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_work_completed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pip_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.pip')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.team')),
            ],
            options={
                'unique_together': {('pip_activity', 'team')},
            },
        ),
        migrations.CreateModel(
            name='MaterialBOQItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('boq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.boq')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.material')),
            ],
            options={
                'unique_together': {('boq', 'material')},
            },
        ),
        migrations.CreateModel(
            name='Deduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause', models.CharField(choices=[('Fine', 'Fine'), ('Damage', 'Damage'), ('Overpayment', 'Overpayment')], max_length=12)),
                ('amount', models.IntegerField()),
                ('description', models.TextField(default='')),
                ('is_manager_approved', models.BooleanField(default=True)),
                ('is_pm_approved', models.BooleanField(null=True)),
                ('is_gm_approved', models.BooleanField(null=True)),
                ('is_payed', models.BooleanField(null=True)),
                ('wage_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.wagesheet')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.worker')),
            ],
            options={
                'unique_together': {('worker', 'wage_sheet')},
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('payment', models.IntegerField()),
                ('description', models.TextField(default='')),
                ('is_manager_approved', models.BooleanField(default=True)),
                ('is_pm_approved', models.BooleanField(null=True)),
                ('is_gm_approved', models.BooleanField(null=True)),
                ('is_payed', models.BooleanField(null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.activity')),
                ('wage_sheet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.wagesheet')),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.worker')),
            ],
            options={
                'unique_together': {('worker', 'wage_sheet', 'activity')},
            },
        ),
        migrations.CreateModel(
            name='ClientActivityRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(default=0)),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('UGX', 'UGX')], default='UGX', max_length=3)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.activity')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
            ],
            options={
                'unique_together': {('client', 'activity')},
            },
        ),
    ]
