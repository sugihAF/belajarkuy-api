# Generated by Django 2.2.1 on 2021-05-30 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0007_remove_assignmenthistory_timestamp'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]
