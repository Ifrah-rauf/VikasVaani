# Generated by Django 4.0.3 on 2024-07-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0017_alter_techcourse_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='test_attempt',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]