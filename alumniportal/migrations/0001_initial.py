# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import alumniportal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('achievement_type', models.CharField(max_length=2, choices=[(b'A', b'Alumni'), (b'I', b'IITG'), (b'S', b'Student')])),
                ('year', models.IntegerField(null=True, blank=True)),
                ('achievement', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-year'],
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_type', models.CharField(max_length=32, choices=[(b'Event', b'Event'), (b'Meet', b'Alumni Meet'), (b'Volunteering', b'Start a Volunteering Activity'), (b'Survey', b'Take a Survey'), (b'Project', b'Float a Project')])),
                ('name', models.CharField(max_length=32)),
                ('purpose', models.CharField(max_length=128)),
                ('image', models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True)),
                ('created', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('requirement', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('images', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True)),
                ('videos', models.TextField(blank=True)),
                ('about_me', models.TextField(blank=True)),
                ('interests', models.TextField(blank=True)),
                ('message_to_the_world', models.TextField(blank=True)),
                ('images', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ClubPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('heading', models.CharField(max_length=64)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('club', models.ForeignKey(related_name='club', to='alumniportal.Club')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=40, choices=[(b'B. Tech', b'B.Tech.'), (b'M. Tech', b'M.Tech.'), (b'B. Des', b'B.Des.'), (b'Ph.D.', b'Ph.D.'), (b'Other', b'Other')])),
                ('institute', models.CharField(max_length=100)),
                ('in_iitg', models.BooleanField()),
                ('start_year', models.IntegerField(null=True)),
                ('end_year', models.IntegerField(null=True)),
                ('department', models.CharField(max_length=50, choices=[(b'bt', b'Biotechnology [BT]'), (b'cl', b'Chemical [CL]'), (b'che', b'Chemistry [CHE]'), (b'ce', b'Civil [CE]'), (b'cse', b'Computer Science [CSE]'), (b'ds', b'Design [DD]'), (b'eee', b'Electrical [EEE]'), (b'ece', b'Electronics [ECE]'), (b'hss', b'Humanities &amp; Social Sciences [HSS]'), (b'ma', b'Mathematics [MA]'), (b'me', b'Mechanical [ME]'), (b'ep', b'Physics [EP]'), (b'cfe', b'Centre for Energy'), (b'cfte', b'Centre for the Environment'), (b'cnt', b'Centre for Nanotechnology'), (b'o', b'Other')])),
                ('specialization', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='IITGExperience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('club_name', models.CharField(max_length=30, choices=[(b'alcheringa', b'Alcheringa'), (b'EDC', b'Entrepreneurial Development Cell (EDC)'), (b'gymkhana', b'Gymkhana'), (b'techniche', b'Techniche'), (b'technothlon', b'Technothlon'), (b'LS', b'Lecture Series'), (b'SAIL', b'Student Alumni Interaction Linkage (SAIL)'), (b'aeromodelling', b'Aeromodeling Club'), (b'astronomy', b'Astronomy Club'), (b'coding', b'Coding Club'), (b'electronics', b'Electronics Club'), (b'prakriti', b'Prakriti Club'), (b'science', b'Science and Quiz Club'), (b'radioG', b'RadioG'), (b'robotics', b'Robotics Club'), (b'finance', b'Finance and Economics Club'), (b'greenAuto', b'Green Automobile Club'), (b'anchoring', b'Anchoring Club'), (b'cadence', b'Cadence Club'), (b'fineArts', b'Fine Arts Club'), (b'litSoc', b'LitSoc'), (b'movie', b'Movie Club'), (b'music', b'Music Club'), (b'xpressions', b'Xpressions'), (b'montage', b'Montage'), (b'publication', b'Publication Subcommittee'), (b'aquatics', b'Aquatics Club'), (b'athletics', b'Athletics Club'), (b'badminton', b'Badminton Club'), (b'basketball', b'Basketball Club'), (b'cricket', b'Cricket Club'), (b'football', b'Football Club'), (b'hockey', b'Hockey Club'), (b'squash', b'Squash Club'), (b'tableTennis', b'Table Tennis Club'), (b'tennis', b'Tennis Club'), (b'volleyball', b'Volleyball Club'), (b'weightlifting', b'Weightlifting Club'), (b'interaction', b'Interaction Club'), (b'benevolence', b'Benevolence Cell'), (b'social', b'Social Service Club'), (b'advisory', b"Students' Advisory Council"), (b'youth', b'Youth Empowerment Club'), (b'rights', b'Rights & Responsibility Club'), (b'counselling', b'Counselling Cell'), (b'redRibbon', b'Red Ribbon Club'), (b'hostel', b'Hostel Affairs Board'), (b'other', b'Other'), (b'Manthan', b'Manthan'), (b'Kriti', b'Manthan')])),
                ('experience', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50, blank=True)),
                ('start_date', models.IntegerField(blank=True, null=True, choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('end_date', models.IntegerField(blank=True, null=True, choices=[(1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014)])),
                ('description', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_type', models.CharField(max_length=2, choices=[(b'I', b'IITG'), (b'A', b'Alumni'), (b'S', b'Student'), (b'R', b'Research'), (b'C', b'Achievement')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('image', models.ImageField(null=True, upload_to=alumniportal.models.get_image_path, blank=True)),
                ('blog', models.ForeignKey(to='alumniportal.Blog')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('profile_type', models.CharField(blank=True, max_length=16, choices=[(b'is_alumni', b'Alumni'), (b'is_stud', b'Current Student'), (b'is_prof', b'Professor')])),
                ('roll_no', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(blank=True, max_length=7, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'o', b'Other')])),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('current_address', models.TextField(blank=True)),
                ('city', models.CharField(max_length=32, blank=True)),
                ('country', models.CharField(max_length=32, blank=True)),
                ('nationality', models.CharField(max_length=32, blank=True)),
                ('alternate_email', models.EmailField(max_length=254, blank=True)),
                ('google_link', models.URLField(blank=True)),
                ('linkedin_link', models.URLField(blank=True)),
                ('facebook_link', models.URLField(blank=True)),
                ('github_link', models.URLField(blank=True)),
                ('twitter_link', models.URLField(blank=True)),
                ('home_contact_no', models.CharField(max_length=15, blank=True)),
                ('work_contact_no', models.CharField(max_length=15, blank=True)),
                ('hostel', models.CharField(blank=True, max_length=15, choices=[(b'Barak', b'Barak'), (b'Brahmaputra', b'Brahmaputra'), (b'Dhansiri', b'Dhansiri'), (b'Dibang', b'Dibang'), (b'Dihing', b'Dihing'), (b'Kameng', b'Kameng'), (b'Kapili', b'Kapili'), (b'Lohit', b'Lohit'), (b'Manas', b'Manas'), (b"Married Scholar's Hostel", b"Married Scholar's Hostel"), (b'Siang', b'Siang'), (b'Subansiri', b'Subansiri'), (b'Umiam', b'Umiam'), (b'Other', b'Other')])),
                ('room_no', models.CharField(max_length=10, blank=True)),
                ('batch', models.CharField(max_length=16, choices=[(b'1998 B.Tech.', b'1998 B.Tech.'), (b'1999 B.Tech.', b'1999 B.Tech.'), (b'2000 B.Tech.', b'2000 B.Tech.'), (b'2001 B.Tech.', b'2001 B.Tech.'), (b'2002 B.Tech.', b'2002 B.Tech.'), (b'2003 B.Tech.', b'2003 B.Tech.'), (b'2004 B.Tech.', b'2004 B.Tech.'), (b'2005 B.Tech.', b'2005 B.Tech.'), (b'2006 B.Tech.', b'2006 B.Tech.'), (b'2007 B.Tech.', b'2007 B.Tech.'), (b'2008 B.Tech.', b'2008 B.Tech.'), (b'2009 B.Tech.', b'2009 B.Tech.'), (b'2010 B.Tech.', b'2010 B.Tech.'), (b'2011 B.Tech.', b'2011 B.Tech.'), (b'2012 B.Tech.', b'2012 B.Tech.'), (b'2013 B.Tech.', b'2013 B.Tech.'), (b'2014 B.Tech.', b'2014 B.Tech.'), (b'2015 B.Tech.', b'2015 B.Tech.'), (b'2016 B.Tech.', b'2016 B.Tech.'), (b'2017 B.Tech.', b'2017 B.Tech.'), (b'2018 B.Tech.', b'2018 B.Tech.'), (b'1998 M.Tech.', b'1998 M.Tech.'), (b'1999 M.Tech.', b'1999 M.Tech.'), (b'2000 M.Tech.', b'2000 M.Tech.'), (b'2001 M.Tech.', b'2001 M.Tech.'), (b'2002 M.Tech.', b'2002 M.Tech.'), (b'2003 M.Tech.', b'2003 M.Tech.'), (b'2004 M.Tech.', b'2004 M.Tech.'), (b'2005 M.Tech.', b'2005 M.Tech.'), (b'2006 M.Tech.', b'2006 M.Tech.'), (b'2007 M.Tech.', b'2007 M.Tech.'), (b'2008 M.Tech.', b'2008 M.Tech.'), (b'2009 M.Tech.', b'2009 M.Tech.'), (b'2010 M.Tech.', b'2010 M.Tech.'), (b'2011 M.Tech.', b'2011 M.Tech.'), (b'2012 M.Tech.', b'2012 M.Tech.'), (b'2013 M.Tech.', b'2013 M.Tech.'), (b'2014 M.Tech.', b'2014 M.Tech.'), (b'2015 M.Tech.', b'2015 M.Tech.'), (b'2016 M.Tech.', b'2016 M.Tech.'), (b'2017 M.Tech.', b'2017 M.Tech.'), (b'2018 M.Tech.', b'2018 M.Tech.'), (b'1998 B.Des.', b'1998 B.Des.'), (b'1999 B.Des.', b'1999 B.Des.'), (b'2000 B.Des.', b'2000 B.Des.'), (b'2001 B.Des.', b'2001 B.Des.'), (b'2002 B.Des.', b'2002 B.Des.'), (b'2003 B.Des.', b'2003 B.Des.'), (b'2004 B.Des.', b'2004 B.Des.'), (b'2005 B.Des.', b'2005 B.Des.'), (b'2006 B.Des.', b'2006 B.Des.'), (b'2007 B.Des.', b'2007 B.Des.'), (b'2008 B.Des.', b'2008 B.Des.'), (b'2009 B.Des.', b'2009 B.Des.'), (b'2010 B.Des.', b'2010 B.Des.'), (b'2011 B.Des.', b'2011 B.Des.'), (b'2012 B.Des.', b'2012 B.Des.'), (b'2013 B.Des.', b'2013 B.Des.'), (b'2014 B.Des.', b'2014 B.Des.'), (b'2015 B.Des.', b'2015 B.Des.'), (b'2016 B.Des.', b'2016 B.Des.'), (b'2017 B.Des.', b'2017 B.Des.'), (b'2018 B.Des.', b'2018 B.Des.'), (b'1998 Ph.D.', b'1998 Ph.D.'), (b'1999 Ph.D.', b'1999 Ph.D.'), (b'2000 Ph.D.', b'2000 Ph.D.'), (b'2001 Ph.D.', b'2001 Ph.D.'), (b'2002 Ph.D.', b'2002 Ph.D.'), (b'2003 Ph.D.', b'2003 Ph.D.'), (b'2004 Ph.D.', b'2004 Ph.D.'), (b'2005 Ph.D.', b'2005 Ph.D.'), (b'2006 Ph.D.', b'2006 Ph.D.'), (b'2007 Ph.D.', b'2007 Ph.D.'), (b'2008 Ph.D.', b'2008 Ph.D.'), (b'2009 Ph.D.', b'2009 Ph.D.'), (b'2010 Ph.D.', b'2010 Ph.D.'), (b'2011 Ph.D.', b'2011 Ph.D.'), (b'2012 Ph.D.', b'2012 Ph.D.'), (b'2013 Ph.D.', b'2013 Ph.D.'), (b'2014 Ph.D.', b'2014 Ph.D.'), (b'2015 Ph.D.', b'2015 Ph.D.'), (b'2016 Ph.D.', b'2016 Ph.D.'), (b'2017 Ph.D.', b'2017 Ph.D.'), (b'2018 Ph.D.', b'2018 Ph.D.'), (b'1998 Other', b'1998 Other'), (b'1999 Other', b'1999 Other'), (b'2000 Other', b'2000 Other'), (b'2001 Other', b'2001 Other'), (b'2002 Other', b'2002 Other'), (b'2003 Other', b'2003 Other'), (b'2004 Other', b'2004 Other'), (b'2005 Other', b'2005 Other'), (b'2006 Other', b'2006 Other'), (b'2007 Other', b'2007 Other'), (b'2008 Other', b'2008 Other'), (b'2009 Other', b'2009 Other'), (b'2010 Other', b'2010 Other'), (b'2011 Other', b'2011 Other'), (b'2012 Other', b'2012 Other'), (b'2013 Other', b'2013 Other'), (b'2014 Other', b'2014 Other'), (b'2015 Other', b'2015 Other'), (b'2016 Other', b'2016 Other'), (b'2017 Other', b'2017 Other'), (b'2018 Other', b'2018 Other')])),
                ('department', models.CharField(blank=True, max_length=25, choices=[(b'bt', b'Biotechnology [BT]'), (b'cl', b'Chemical [CL]'), (b'che', b'Chemistry [CHE]'), (b'ce', b'Civil [CE]'), (b'cse', b'Computer Science [CSE]'), (b'ds', b'Design [DD]'), (b'eee', b'Electrical [EEE]'), (b'ece', b'Electronics [ECE]'), (b'hss', b'Humanities &amp; Social Sciences [HSS]'), (b'ma', b'Mathematics [MA]'), (b'me', b'Mechanical [ME]'), (b'ep', b'Physics [EP]'), (b'cfe', b'Centre for Energy'), (b'cfte', b'Centre for the Environment'), (b'cnt', b'Centre for Nanotechnology'), (b'o', b'Other')])),
                ('current_education', models.OneToOneField(related_name='current_education', null=True, blank=True, to='alumniportal.Education')),
                ('current_job', models.OneToOneField(related_name='current_job', null=True, blank=True, to='alumniportal.Job')),
                ('user', models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=128)),
                ('mentor', models.CharField(max_length=32, blank=True)),
                ('description', models.TextField(blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('profile', models.ForeignKey(related_name='projects', blank=True, to='alumniportal.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('week', models.CharField(max_length=6, unique=True, serialize=False, primary_key=True)),
            ],
            options={
                'ordering': ['-week'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='recent',
            field=models.ForeignKey(related_name='projects', blank=True, to='alumniportal.Recent'),
        ),
        migrations.AddField(
            model_name='post',
            name='recent',
            field=models.ForeignKey(related_name='posts', blank=True, to='alumniportal.Recent'),
        ),
        migrations.AddField(
            model_name='news',
            name='recent',
            field=models.ForeignKey(related_name='news', blank=True, to='alumniportal.Recent'),
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(related_name='jobs', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='iitgexperience',
            name='profile',
            field=models.ForeignKey(related_name='iitgexperiences', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(related_name='educations', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='clubpost',
            name='member',
            field=models.ForeignKey(related_name='clubposts', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='profile',
            field=models.OneToOneField(blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='activity',
            name='peoples_involved',
            field=models.ManyToManyField(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='profile',
            field=models.ForeignKey(related_name='activities', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='activity',
            name='recent',
            field=models.ForeignKey(related_name='activities', blank=True, to='alumniportal.Recent'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='profile',
            field=models.ForeignKey(related_name='achievements', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='achievement',
            name='recent',
            field=models.ForeignKey(related_name='achievements', blank=True, to='alumniportal.Recent'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='post',
            order_with_respect_to='recent',
        ),
        migrations.AlterOrderWithRespectTo(
            name='news',
            order_with_respect_to='recent',
        ),
        migrations.AlterOrderWithRespectTo(
            name='activity',
            order_with_respect_to='recent',
        ),
        migrations.AlterOrderWithRespectTo(
            name='achievement',
            order_with_respect_to='recent',
        ),
    ]
