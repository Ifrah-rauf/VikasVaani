# Generated by Django 4.0.3 on 2024-07-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_alter_user_data_test_attempt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngo',
            name='note',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]