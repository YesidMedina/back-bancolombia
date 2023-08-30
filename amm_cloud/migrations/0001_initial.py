# Generated by Django 4.2.3 on 2023-07-16 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmmCloudModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(max_length=2)),
                ('tool', models.CharField(max_length=50)),
                ('global_collection', models.CharField(max_length=50)),
                ('filial', models.CharField(max_length=50)),
                ('modulo', models.CharField(max_length=50)),
                ('service_manager', models.CharField(max_length=200)),
                ('sub_service', models.CharField(max_length=200)),
                ('name_alert_back', models.CharField(max_length=200)),
                ('name_alert', models.CharField(max_length=100)),
                ('type_configuration', models.CharField(max_length=100)),
                ('item_configuration', models.CharField(max_length=100)),
                ('value_configuration', models.CharField(max_length=100)),
                ('condition_alert', models.CharField(max_length=50)),
                ('frequencie', models.CharField(max_length=50)),
                ('alert_hours', models.CharField(max_length=100)),
                ('major', models.CharField(max_length=100)),
                ('critical', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('impact', models.CharField(max_length=500)),
                ('details_query', models.CharField(max_length=500)),
                ('reference_document', models.CharField(max_length=200)),
                ('type_location', models.CharField(max_length=50)),
                ('test_location', models.CharField(max_length=50)),
                ('spectrum', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('order_number_oc', models.CharField(max_length=500)),
                ('state_newrelic', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'amm_cloud',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='EmailAmmCloudModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_email', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email_notification', models.CharField(max_length=500)),
                ('order_oc', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'email_amm_cloud',
                'ordering': ['-created_at'],
            },
        ),
    ]
