# Generated by Django 3.2 on 2021-04-14 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrs', '0009_searchmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchmodel',
            name='user',
        ),
    ]
