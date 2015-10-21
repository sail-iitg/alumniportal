# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0003_auto_20151021_1450'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='date',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='profile',
            new_name='blog',
        ),
    ]
