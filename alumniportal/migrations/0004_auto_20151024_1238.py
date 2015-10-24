# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0003_auto_20151024_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='roll_no',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
