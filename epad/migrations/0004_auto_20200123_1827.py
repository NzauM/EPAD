# Generated by Django 2.0 on 2020-01-23 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epad', '0003_auto_20200122_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='employed_on',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='pictures/'),
        ),
    ]
