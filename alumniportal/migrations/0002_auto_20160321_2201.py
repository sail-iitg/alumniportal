# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='current_education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='current_job',
        ),
        migrations.AddField(
            model_name='profile',
            name='currentEducation',
            field=models.OneToOneField(related_name='currentEducation', null=True, blank=True, to='alumniportal.Education'),
        ),
        migrations.AddField(
            model_name='profile',
            name='currentJob',
            field=models.OneToOneField(related_name='currentJob', null=True, blank=True, to='alumniportal.Job'),
        ),
        migrations.AlterField(
            model_name='job',
            name='end_date',
            field=models.IntegerField(blank=True, null=True, choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)]),
        ),
        migrations.AlterField(
            model_name='job',
            name='start_date',
            field=models.IntegerField(choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015)]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='batch',
            field=models.CharField(max_length=16, choices=[(b'1998 B.Tech.', b'1998 B.Tech.'), (b'1999 B.Tech.', b'1999 B.Tech.'), (b'2000 B.Tech.', b'2000 B.Tech.'), (b'2001 B.Tech.', b'2001 B.Tech.'), (b'2002 B.Tech.', b'2002 B.Tech.'), (b'2003 B.Tech.', b'2003 B.Tech.'), (b'2004 B.Tech.', b'2004 B.Tech.'), (b'2005 B.Tech.', b'2005 B.Tech.'), (b'2006 B.Tech.', b'2006 B.Tech.'), (b'2007 B.Tech.', b'2007 B.Tech.'), (b'2008 B.Tech.', b'2008 B.Tech.'), (b'2009 B.Tech.', b'2009 B.Tech.'), (b'2010 B.Tech.', b'2010 B.Tech.'), (b'2011 B.Tech.', b'2011 B.Tech.'), (b'2012 B.Tech.', b'2012 B.Tech.'), (b'2013 B.Tech.', b'2013 B.Tech.'), (b'2014 B.Tech.', b'2014 B.Tech.'), (b'2015 B.Tech.', b'2015 B.Tech.'), (b'2016 B.Tech.', b'2016 B.Tech.'), (b'2017 B.Tech.', b'2017 B.Tech.'), (b'2018 B.Tech.', b'2018 B.Tech.'), (b'2019 B.Tech.', b'2019 B.Tech.'), (b'1998 M.Tech.', b'1998 M.Tech.'), (b'1999 M.Tech.', b'1999 M.Tech.'), (b'2000 M.Tech.', b'2000 M.Tech.'), (b'2001 M.Tech.', b'2001 M.Tech.'), (b'2002 M.Tech.', b'2002 M.Tech.'), (b'2003 M.Tech.', b'2003 M.Tech.'), (b'2004 M.Tech.', b'2004 M.Tech.'), (b'2005 M.Tech.', b'2005 M.Tech.'), (b'2006 M.Tech.', b'2006 M.Tech.'), (b'2007 M.Tech.', b'2007 M.Tech.'), (b'2008 M.Tech.', b'2008 M.Tech.'), (b'2009 M.Tech.', b'2009 M.Tech.'), (b'2010 M.Tech.', b'2010 M.Tech.'), (b'2011 M.Tech.', b'2011 M.Tech.'), (b'2012 M.Tech.', b'2012 M.Tech.'), (b'2013 M.Tech.', b'2013 M.Tech.'), (b'2014 M.Tech.', b'2014 M.Tech.'), (b'2015 M.Tech.', b'2015 M.Tech.'), (b'2016 M.Tech.', b'2016 M.Tech.'), (b'2017 M.Tech.', b'2017 M.Tech.'), (b'2018 M.Tech.', b'2018 M.Tech.'), (b'2019 M.Tech.', b'2019 M.Tech.'), (b'1998 B.Des.', b'1998 B.Des.'), (b'1999 B.Des.', b'1999 B.Des.'), (b'2000 B.Des.', b'2000 B.Des.'), (b'2001 B.Des.', b'2001 B.Des.'), (b'2002 B.Des.', b'2002 B.Des.'), (b'2003 B.Des.', b'2003 B.Des.'), (b'2004 B.Des.', b'2004 B.Des.'), (b'2005 B.Des.', b'2005 B.Des.'), (b'2006 B.Des.', b'2006 B.Des.'), (b'2007 B.Des.', b'2007 B.Des.'), (b'2008 B.Des.', b'2008 B.Des.'), (b'2009 B.Des.', b'2009 B.Des.'), (b'2010 B.Des.', b'2010 B.Des.'), (b'2011 B.Des.', b'2011 B.Des.'), (b'2012 B.Des.', b'2012 B.Des.'), (b'2013 B.Des.', b'2013 B.Des.'), (b'2014 B.Des.', b'2014 B.Des.'), (b'2015 B.Des.', b'2015 B.Des.'), (b'2016 B.Des.', b'2016 B.Des.'), (b'2017 B.Des.', b'2017 B.Des.'), (b'2018 B.Des.', b'2018 B.Des.'), (b'2019 B.Des.', b'2019 B.Des.'), (b'1998 Ph.D.', b'1998 Ph.D.'), (b'1999 Ph.D.', b'1999 Ph.D.'), (b'2000 Ph.D.', b'2000 Ph.D.'), (b'2001 Ph.D.', b'2001 Ph.D.'), (b'2002 Ph.D.', b'2002 Ph.D.'), (b'2003 Ph.D.', b'2003 Ph.D.'), (b'2004 Ph.D.', b'2004 Ph.D.'), (b'2005 Ph.D.', b'2005 Ph.D.'), (b'2006 Ph.D.', b'2006 Ph.D.'), (b'2007 Ph.D.', b'2007 Ph.D.'), (b'2008 Ph.D.', b'2008 Ph.D.'), (b'2009 Ph.D.', b'2009 Ph.D.'), (b'2010 Ph.D.', b'2010 Ph.D.'), (b'2011 Ph.D.', b'2011 Ph.D.'), (b'2012 Ph.D.', b'2012 Ph.D.'), (b'2013 Ph.D.', b'2013 Ph.D.'), (b'2014 Ph.D.', b'2014 Ph.D.'), (b'2015 Ph.D.', b'2015 Ph.D.'), (b'2016 Ph.D.', b'2016 Ph.D.'), (b'2017 Ph.D.', b'2017 Ph.D.'), (b'2018 Ph.D.', b'2018 Ph.D.'), (b'2019 Ph.D.', b'2019 Ph.D.'), (b'1998 Other', b'1998 Other'), (b'1999 Other', b'1999 Other'), (b'2000 Other', b'2000 Other'), (b'2001 Other', b'2001 Other'), (b'2002 Other', b'2002 Other'), (b'2003 Other', b'2003 Other'), (b'2004 Other', b'2004 Other'), (b'2005 Other', b'2005 Other'), (b'2006 Other', b'2006 Other'), (b'2007 Other', b'2007 Other'), (b'2008 Other', b'2008 Other'), (b'2009 Other', b'2009 Other'), (b'2010 Other', b'2010 Other'), (b'2011 Other', b'2011 Other'), (b'2012 Other', b'2012 Other'), (b'2013 Other', b'2013 Other'), (b'2014 Other', b'2014 Other'), (b'2015 Other', b'2015 Other'), (b'2016 Other', b'2016 Other'), (b'2017 Other', b'2017 Other'), (b'2018 Other', b'2018 Other'), (b'2019 Other', b'2019 Other')]),
        ),
    ]
