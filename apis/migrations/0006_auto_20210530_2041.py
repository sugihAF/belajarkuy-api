# Generated by Django 2.2.1 on 2021-05-30 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0005_auto_20210530_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulesstatus',
            name='modules',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulesstatus_modules', to='apis.Modules'),
        ),
    ]
