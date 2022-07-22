# Generated by Django 4.0.6 on 2022-07-19 15:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='occ_name', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='occ_created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='occ_updated_at')),
                ('company', models.ForeignKey(db_column='occ_id_company_fk', default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='companies.company')),
            ],
            options={
                'db_table': 'tbl_occupations',
            },
        ),
    ]
