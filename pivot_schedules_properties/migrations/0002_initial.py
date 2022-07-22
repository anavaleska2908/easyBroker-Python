# Generated by Django 4.0.6 on 2022-07-19 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pivot_schedules_properties', '0001_initial'),
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pivotschedulesproperties',
            name='schedule',
            field=models.ForeignKey(db_column='puc_id_schedule_fk', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='schedules.schedule'),
        ),
    ]