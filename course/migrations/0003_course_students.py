# Generated by Django 4.0.6 on 2022-11-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_myuser_pdp'),
        ('course', '0002_course_date_upload_alter_subject_subject_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.student'),
        ),
    ]
