# Generated by Django 3.2 on 2021-04-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrs', '0003_auto_20210413_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='uid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
