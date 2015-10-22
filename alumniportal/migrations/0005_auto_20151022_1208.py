# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import alumniportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0004_auto_20151022_0624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recent',
            name='activities',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True),
        ),
        migrations.AlterField(
            model_name='achievement',
            name='recent',
            field=models.ForeignKey(related_name='achievements', blank=True, to='alumniportal.Recent'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='profile',
            field=models.ForeignKey(related_name='activities', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='recent',
            field=models.ForeignKey(related_name='activities', default=1, blank=True, to='alumniportal.Recent'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(max_length=2, choices=[(b'U', b'University'), (b'A', b'Alumni'), (b'S', b'Student'), (b'R', b'Research'), (b'B', b'Blog')]),
        ),
        migrations.AlterField(
            model_name='post',
            name='recent',
            field=models.ForeignKey(related_name='posts', blank=True, to='alumniportal.Recent'),
        ),
        migrations.AlterField(
            model_name='project',
            name='recent',
            field=models.ForeignKey(related_name='projects', blank=True, to='alumniportal.Recent'),
        ),
    ]
