# Generated by Django 4.0.6 on 2022-11-17 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_title', models.CharField(max_length=20, verbose_name='department')),
                ('dept_slug', models.SlugField()),
                ('dept_desc', models.TextField(blank=True, verbose_name='desc')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='price')),
            ],
        ),
    ]
