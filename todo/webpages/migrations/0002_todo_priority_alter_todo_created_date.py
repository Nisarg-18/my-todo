# Generated by Django 4.0.2 on 2022-02-06 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('Urgent', 'Urgent'), ('EOD', 'EOD'), ('No Deadline', 'No Deadline')], default='No Deadline', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 6, 19, 53, 19, 182429)),
        ),
    ]
