# Generated by Django 4.0.3 on 2024-07-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_report_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='ngo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('location', models.CharField(max_length=225)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='seminars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('organizer', models.CharField(max_length=225)),
                ('date', models.DateField()),
                ('link', models.URLField()),
            ],
        ),
    ]