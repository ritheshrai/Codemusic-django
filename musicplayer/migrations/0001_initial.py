# Generated by Django 3.1.4 on 2020-12-07 08:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('songList', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='playlistCON',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playlistcollection', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('musicID', models.CharField(max_length=50)),
                ('musicTitle', models.CharField(max_length=100)),
                ('musicDESC', models.TextField()),
                ('musicIMG', models.URLField()),
                ('musicUrl', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicplayer.playlistcon')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
