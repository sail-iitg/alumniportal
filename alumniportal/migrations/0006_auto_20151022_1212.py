# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0005_auto_20151022_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(blank=True, max_length=16, choices=[(b'is_iitg', b'IITG'), (b'is_alumni', b'Alumni'), (b'is_stud', b'Current Student'), (b'is_prof', b'Professor')]),
        ),
    ]
