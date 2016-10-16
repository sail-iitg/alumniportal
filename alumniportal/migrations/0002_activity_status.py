# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='status',
            field=models.CharField(default=1, max_length=16, choices=[(b'Accepted', b'Accepted'), (b'Denied', b'Denied'), (b'Pending', b'Pending')]),
            preserve_default=False,
        ),
    ]
