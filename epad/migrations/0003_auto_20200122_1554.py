# Generated by Django 2.0 on 2020-01-22 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('epad', '0002_kpis_tasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kpis',
            old_name='absenteeism',
            new_name='punctuality',
        ),
        migrations.RenameField(
            model_name='kpis',
            old_name='user',
            new_name='rates_for',
        ),
        migrations.RenameField(
            model_name='kpis',
            old_name='objectives',
            new_name='soft_skills',
        ),
    ]
