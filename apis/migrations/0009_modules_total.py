# Generated by Django 2.2.1 on 2021-05-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0008_delete_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='modules',
            name='total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
