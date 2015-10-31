# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0002_auto_20151024_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='institute',
            field=models.CharField(default=b'IIT Guwahati', max_length=100),
        ),
    ]
