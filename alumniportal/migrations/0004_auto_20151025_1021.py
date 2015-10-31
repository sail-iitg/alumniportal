# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0003_auto_20151024_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='institute',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='recent',
            field=models.ForeignKey(related_name='posts', blank=True, to='alumniportal.Recent', null=True),
        ),
    ]
