# Generated by Django 4.0.6 on 2022-11-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='date_upload',
            field=models.DateTimeField(auto_now=True, verbose_name='date upload'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='subject_name',
            field=models.CharField(max_length=100, verbose_name='subject'),
        ),
    ]
