# Generated by Django 2.2.1 on 2021-05-30 07:20

from django.db import migrations, models
import django.db.models.deletion
import django_spanner


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Modules',
            fields=[
                ('id', models.AutoField(auto_created=True, default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=233)),
                ('classes', models.CharField(max_length=233)),
                ('modules', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_question', models.CharField(max_length=233)),
                ('questionOnly', models.CharField(max_length=233)),
                ('option_1', models.CharField(max_length=233)),
                ('option_2', models.CharField(max_length=233)),
                ('option_3', models.CharField(max_length=233)),
                ('option_4', models.CharField(max_length=233)),
                ('answer', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=233)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemistry', models.FloatField()),
                ('mathematics', models.FloatField()),
                ('biology', models.FloatField()),
                ('physics', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_user', to='apis.User')),
            ],
        ),
        migrations.CreateModel(
            name='ModulesStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('modules', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules_status', to='apis.Modules')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules_user', to='apis.User')),
            ],
        ),
        migrations.AddField(
            model_name='modules',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='apis.Question'),
        ),
        migrations.CreateModel(
            name='AssignmentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, default=django_spanner.gen_rand_int64, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('timestamp', models.DateTimeField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_history_question', to='apis.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignment_history_user', to='apis.User')),
            ],
        ),
    ]
