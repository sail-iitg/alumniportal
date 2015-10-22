# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0003_auto_20151022_0608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='recent',
            field=models.ForeignKey(blank=True, to='alumniportal.Recent', null=True),
        ),
    ]
