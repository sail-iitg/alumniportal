# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import alumniportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=alumniportal.models.get_image_path)),
            ],
        ),
        migrations.CreateModel(
            name='NewsImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=alumniportal.models.get_image_path)),
                ('news', models.ForeignKey(related_name='images', to='alumniportal.News')),
            ],
        ),
        migrations.RemoveField(
            model_name='activity',
            name='images',
        ),
        migrations.AddField(
            model_name='activityimage',
            name='activity',
            field=models.ForeignKey(related_name='images', to='alumniportal.Activity'),
        ),
    ]
