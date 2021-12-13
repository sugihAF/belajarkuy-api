# Generated by Django 2.2.1 on 2021-05-30 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0004_question_chapter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modules',
            name='classes',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='modules',
            name='subject',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='question',
            name='chapter',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='question',
            name='full_question',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.CharField(max_length=512, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_1',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_2',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_3',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_4',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionOnly',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=512),
        ),
    ]