# Generated by Django 4.2.4 on 2023-09-03 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revise_minder', '0007_study_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='color',
            field=models.CharField(choices=[('vermelho', '🔴 Vermelho'), ('laranja', '🟠 Laranja'), ('amarelo', '🟡 Amarelo'), ('verde', '🟢 Verde'), ('azul', '🔵 Azul'), ('roxo', '🟣 Roxo'), ('branco', '⚪ Branco')], default='', max_length=100),
        ),
    ]
