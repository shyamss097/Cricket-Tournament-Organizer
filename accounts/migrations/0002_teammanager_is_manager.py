# Generated by Django 4.1.3 on 2023-01-09 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammanager',
            name='is_manager',
            field=models.BooleanField(default=True),
        ),
    ]
