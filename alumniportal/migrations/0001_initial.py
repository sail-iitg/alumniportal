# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('year', models.IntegerField(null=True, blank=True)),
                ('achievement', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_type', models.CharField(max_length=32, choices=[(b'Event', b'Event'), (b'Meet', b'Alumni Meet'), (b'Volunteering', b'Start a Volunteering Activity'), (b'Survey', b'Take a Survey'), (b'Project', b'Float a Project')])),
                ('name', models.CharField(max_length=32)),
                ('purpose', models.CharField(max_length=128)),
                ('date', models.DateTimeField(blank=True)),
                ('end_date', models.DateTimeField(null=True, blank=True)),
                ('requirement', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('images', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'', blank=True)),
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
                ('posts', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('degree', models.CharField(max_length=40, choices=[(b'b', b'B.Tech.'), (b'm', b'M.Tech.'), (b'bd', b'B.Des.'), (b'p', b'Ph.D.'), (b'other', b'Other')])),
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
                ('club_name', models.CharField(max_length=30, choices=[(b'alcheringa', b'Alcheringa'), (b'EDC', b'Entrepreneurial Development Cell (EDC)'), (b'gymkhana', b'Gymkhana'), (b'techniche', b'Techniche'), (b'SAIL', b'Student Alumni Interaction Linkage (SAIL)'), (b'aeromodelling', b'Aeromodeling Club'), (b'astronomy', b'Astronomy Club'), (b'coding', b'Coding Club'), (b'electronics', b'Electronics Club'), (b'prakriti', b'Prakriti Club'), (b'science', b'Science and Quiz Club'), (b'radioG', b'RadioG'), (b'robotics', b'Robotics Club'), (b'finance', b'Finance and Economics Club'), (b'greenAuto', b'Green Automobile Club'), (b'anchoring', b'Anchoring Club'), (b'cadence', b'Cadence Club'), (b'fineArts', b'Fine Arts Club'), (b'litSoc', b'LitSoc'), (b'movie', b'Movie Club'), (b'music', b'Music Club'), (b'xpressions', b'Xpressions'), (b'montage', b'Montage'), (b'publication', b'Publication Subcommittee'), (b'aquatics', b'Aquatics Club'), (b'athletics', b'Athletics Club'), (b'badminton', b'Badminton Club'), (b'basketball', b'Basketball Club'), (b'cricket', b'Cricket Club'), (b'football', b'Football Club'), (b'hockey', b'Hockey Club'), (b'squash', b'Squash Club'), (b'tableTennis', b'Table Tennis Club'), (b'tennis', b'Tennis Club'), (b'volleyball', b'Volleyball Club'), (b'weightlifting', b'Weightlifting Club'), (b'interaction', b'Interaction Club'), (b'benevolence', b'Benevolence Cell'), (b'social', b'Social Service Club'), (b'advisory', b"Students' Advisory Council"), (b'youth', b'Youth Empowerment Club'), (b'rights', b'Rights & Responsibility Club'), (b'counselling', b'Counselling Cell'), (b'redRibbon', b'Red Ribbon Club'), (b'hostel', b'Hostel Affairs Board'), (b'other', b'Other')])),
                ('experience', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=50)),
                ('position', models.CharField(max_length=50, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
                ('description', models.CharField(max_length=50, blank=True)),
                ('city', models.CharField(max_length=50, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('heading', models.CharField(max_length=128)),
                ('content', models.TextField()),
                ('profile', models.ForeignKey(to='alumniportal.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('roll_no', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=7, choices=[(b'm', b'Male'), (b'f', b'Female'), (b'o', b'Other')])),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('current_job_id', models.IntegerField(unique=True, null=True, blank=True)),
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
                ('hostel', models.CharField(max_length=15, choices=[(b'Barak', b'Barak'), (b'Brahmaputra', b'Brahmaputra'), (b'Dhansiri', b'Dhansiri'), (b'Dibang', b'Dibang'), (b'Dihing', b'Dihing'), (b'Kameng', b'Kameng'), (b'Kapili', b'Kapili'), (b'Lohit', b'Lohit'), (b'Manas', b'Manas'), (b"Married Scholar's Hostel", b"Married Scholar's Hostel"), (b'Siang', b'Siang'), (b'Subansiri', b'Subansiri'), (b'Umiam', b'Umiam'), (b'Other', b'Other')])),
                ('room_no', models.CharField(max_length=10, blank=True)),
                ('batch', models.IntegerField(choices=[(98, 1998), (99, 1999), (0, 2000), (1, 2001), (2, 2002), (3, 2003), (4, 2004), (5, 2005), (6, 2006), (7, 2007), (8, 2008), (9, 2009), (10, 2010), (11, 2011), (12, 2012), (13, 2013), (14, 2014), (15, 2015), (16, 2016), (17, 2017), (18, 2018), (19, 2019), (20, 2020)])),
                ('department', models.CharField(max_length=25, choices=[(b'bt', b'Biotechnology [BT]'), (b'cl', b'Chemical [CL]'), (b'che', b'Chemistry [CHE]'), (b'ce', b'Civil [CE]'), (b'cse', b'Computer Science [CSE]'), (b'ds', b'Design [DD]'), (b'eee', b'Electrical [EEE]'), (b'ece', b'Electronics [ECE]'), (b'hss', b'Humanities &amp; Social Sciences [HSS]'), (b'ma', b'Mathematics [MA]'), (b'me', b'Mechanical [ME]'), (b'ep', b'Physics [EP]'), (b'cfe', b'Centre for Energy'), (b'cfte', b'Centre for the Environment'), (b'cnt', b'Centre for Nanotechnology'), (b'o', b'Other')])),
                ('blog_id', models.OneToOneField(blank=True, to='alumniportal.Blog')),
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
                ('profile', models.ForeignKey(to='alumniportal.Profile', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('week', models.CharField(max_length=6, unique=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='project',
            name='recent',
            field=models.ForeignKey(to='alumniportal.Recent', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='recent',
            field=models.ForeignKey(to='alumniportal.Recent', blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='profile',
            field=models.ForeignKey(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='iitgexperience',
            name='profile',
            field=models.ForeignKey(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='education',
            name='profile',
            field=models.ForeignKey(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='club',
            name='members',
            field=models.ManyToManyField(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='peoples_involved',
            field=models.ManyToManyField(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='profile',
            field=models.ForeignKey(related_name='activity_host', blank=True, to='alumniportal.Profile'),
        ),
        migrations.AddField(
            model_name='activity',
            name='recent',
            field=models.ForeignKey(to='alumniportal.Recent', blank=True),
        ),
        migrations.AddField(
            model_name='achievement',
            name='profile',
            field=models.ForeignKey(to='alumniportal.Profile', blank=True),
        ),
        migrations.AddField(
            model_name='achievement',
            name='recent',
            field=models.ForeignKey(to='alumniportal.Recent', blank=True),
        ),
    ]
