# Generated by Django 2.2.1 on 2021-05-30 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_auto_20210530_2041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmenthistory',
            name='timestamp',
        ),
    ]
