# Generated by Django 4.2.4 on 2023-09-17 01:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('revise_minder', '0013_revision_user_alter_study_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='revision',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_revision', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='study',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_study', to=settings.AUTH_USER_MODEL),
        ),
    ]
