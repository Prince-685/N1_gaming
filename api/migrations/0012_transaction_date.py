# Generated by Django 4.1.2 on 2023-12-26 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_win_percent'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='date',
            field=models.DateField(default='2000-01-01'),
            preserve_default=False,
        ),
    ]
