# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roll_no',
            field=models.CharField(max_length=16, unique=True, serialize=False, primary_key=True),
        ),
    ]
