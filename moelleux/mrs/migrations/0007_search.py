# Generated by Django 3.2 on 2021-04-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mrs', '0006_delete_search'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=50)),
                ('song_artist', models.CharField(max_length=100)),
            ],
        ),
    ]