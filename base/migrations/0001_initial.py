# Generated by Django 4.2.3 on 2023-08-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Institut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
                ('categorie', models.TextField()),
                ('desription', models.TextField()),
            ],
            options={
                'verbose_name': 'Institut',
                'verbose_name_plural': 'Instituts',
            },
        ),
    ]
