# Generated by Django 4.0.5 on 2022-06-21 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(blank=True, max_length=200, null=True)),
                ('connected_player', models.IntegerField(default=0, null=True)),
                ('active_player', models.CharField(blank=True, max_length=200, null=True)),
                ('board', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]