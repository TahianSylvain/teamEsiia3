# Generated by Django 4.0.6 on 2022-11-17 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=20, verbose_name='subject')),
                ('subject_slug', models.SlugField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.department', verbose_name='subject department')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.teacher', verbose_name='teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField()),
                ('description', models.TextField(verbose_name='desc')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='courses/cover')),
                ('video', models.FileField(blank=True, null=True, upload_to='courses/video')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.subject', verbose_name='subject')),
            ],
        ),
    ]
