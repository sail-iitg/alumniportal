# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import alumniportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0011_auto_20151023_0121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='activity',
            name='image',
            field=models.ImageField(default=1, upload_to=alumniportal.models.get_image_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(max_length=2, choices=[(b'I', b'IITG'), (b'A', b'Alumni'), (b'S', b'Student'), (b'R', b'Research'), (b'B', b'Blog')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='activity',
            order_with_respect_to='recent',
        ),
    ]
