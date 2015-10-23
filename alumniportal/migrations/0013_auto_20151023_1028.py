# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import alumniportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0012_auto_20151023_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True),
        ),
    ]
