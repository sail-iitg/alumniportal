# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import alumniportal.models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0013_auto_20151023_1028'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_type', models.CharField(max_length=2, choices=[(b'I', b'IITG'), (b'A', b'Alumni'), (b'S', b'Student'), (b'R', b'Research'), (b'B', b'Blog')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True)),
                ('recent', models.ForeignKey(related_name='news', blank=True, to='alumniportal.Recent')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterOrderWithRespectTo(
            name='news',
            order_with_respect_to='recent',
        ),
    ]
