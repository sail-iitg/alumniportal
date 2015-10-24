# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='recent',
            field=models.ForeignKey(related_name='news', blank=True, to='alumniportal.Recent', null=True),
        ),
    ]
