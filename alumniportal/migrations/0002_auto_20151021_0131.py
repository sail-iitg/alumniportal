# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='blog_id',
            new_name='blog',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='current_job_id',
        ),
        migrations.AddField(
            model_name='profile',
            name='current_job',
            field=models.OneToOneField(related_name='job', null=True, blank=True, to='alumniportal.Job'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to=b'profile_picture/%s', blank=True),
        ),
    ]
