# Generated by Django 4.1.2 on 2023-12-17 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_win_percent_earn_point_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='earn_point',
            name='earnpoint',
        ),
    ]
