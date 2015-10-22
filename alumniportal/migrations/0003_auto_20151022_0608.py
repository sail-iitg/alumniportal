# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0002_remove_activity_recent'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='recent',
            field=models.ForeignKey(default=1234, blank=True, to='alumniportal.Recent'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='recent',
            name='activities',
            field=models.TextField(default=(['yash', 'yash_id'],)),
            preserve_default=False,
        ),
    ]
