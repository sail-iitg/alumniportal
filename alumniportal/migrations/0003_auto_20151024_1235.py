# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import alumniportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0002_auto_20151024_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='image',
            field=models.ImageField(default=1, upload_to=alumniportal.models.get_image_path),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='roll_no',
            field=models.IntegerField(unique=True),
        ),
    ]
