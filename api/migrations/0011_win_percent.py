# Generated by Django 4.1.2 on 2023-12-19 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_delete_win_percent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Win_Percent',
            fields=[
                ('percent', models.IntegerField()),
                ('pid', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
