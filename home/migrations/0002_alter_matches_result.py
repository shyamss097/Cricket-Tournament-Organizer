# Generated by Django 4.1.3 on 2023-01-09 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matches',
            name='result',
            field=models.CharField(blank=True, choices=[('A', 'Team A won'), ('B', 'Team B won'), ('D', 'Draw')], max_length=1, null=True),
        ),
    ]
