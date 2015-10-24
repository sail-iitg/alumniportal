# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0002_auto_20151023_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
