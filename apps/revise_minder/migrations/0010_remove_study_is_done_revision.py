# Generated by Django 4.2.4 on 2023-09-06 23:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('revise_minder', '0009_subject_user_alter_study_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='is_done',
        ),
        migrations.CreateModel(
            name='Revision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('date_plus_1_day', models.DateField(default=None)),
                ('date_plus_1_week', models.DateField(blank=True, default=None, null=True)),
                ('date_plus_1_month', models.DateField(blank=True, default=None, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('study', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='study_revision', to='revise_minder.study')),
            ],
        ),
    ]