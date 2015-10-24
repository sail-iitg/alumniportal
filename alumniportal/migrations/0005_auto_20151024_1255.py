# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0004_auto_20151024_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_year',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.IntegerField(default=1, choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)]),
            preserve_default=False,
        ),
    ]
