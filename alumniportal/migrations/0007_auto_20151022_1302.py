# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0006_auto_20151022_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='achievement',
            name='achievement_type',
            field=models.CharField(default=1, max_length=2, choices=[(b'A', b'Alumni'), (b'I', b'IITG'), (b'S', b'Student')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='batch',
            field=models.IntegerField(choices=[(1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)]),
        ),
    ]
