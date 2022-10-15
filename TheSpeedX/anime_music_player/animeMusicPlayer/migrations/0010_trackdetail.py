# Generated by Django 2.2.7 on 2019-11-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animeMusicPlayer', '0009_delete_trackdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trackdetail',
            fields=[
                ('songId', models.AutoField(primary_key=True, serialize=False)),
                ('trackName', models.CharField(max_length=64, unique=True)),
                ('trackPath', models.CharField(max_length=256, unique=True)),
                ('artworkPath', models.CharField(max_length=256, unique=True)),
                ('artistName', models.CharField(max_length=64)),
            ],
        ),
    ]
