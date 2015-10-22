# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0008_auto_20151022_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.IntegerField(blank=True, null=True, choices=[(3988, 3988), (3989, 3989), (3990, 3990), (3991, 3991), (3992, 3992), (3993, 3993), (3994, 3994), (3995, 3995), (3996, 3996), (3997, 3997), (3998, 3998), (3999, 3999), (4000, 4000), (4001, 4001), (4002, 4002), (4003, 4003), (4004, 4004), (4005, 4005), (4006, 4006), (4007, 4007), (4008, 4008)]),
        ),
    ]
