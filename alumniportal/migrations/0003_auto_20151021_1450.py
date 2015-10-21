# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alumniportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0002_auto_20151021_0131'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(default=1, max_length=2, choices=[(b'U', b'University'), (b'A', b'Alumni'), (b'S', b'Student'), (b'R', b'Research')]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(default=1, max_length=2, choices=[(b'is_iitg', b'IITG'), (b'is_alumni', b'Alumni'), (b'is_stud', b'Current Student'), (b'is_prof', b'Professor')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True),
        ),
    ]
