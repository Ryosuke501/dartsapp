# Generated by Django 3.2.23 on 2023-11-15 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dartsgames', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game_result',
            name='round',
            field=models.PositiveIntegerField(null=True, verbose_name='ラウンド'),
        ),
        migrations.AlterField(
            model_name='game_result',
            name='score',
            field=models.IntegerField(null=True, verbose_name='スコア'),
        ),
    ]
