# Generated by Django 3.2 on 2021-04-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrs', '0018_searchmodel_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feedback', models.TextField()),
            ],
        ),
    ]