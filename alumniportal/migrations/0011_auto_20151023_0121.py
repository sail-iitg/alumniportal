# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alumniportal', '0010_auto_20151022_2025'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='achievement',
            options={'ordering': ['-year']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AlterModelOptions(
            name='recent',
            options={'ordering': ['-week']},
        ),
        migrations.AlterField(
            model_name='iitgexperience',
            name='club_name',
            field=models.CharField(max_length=30, choices=[(b'alcheringa', b'Alcheringa'), (b'EDC', b'Entrepreneurial Development Cell (EDC)'), (b'gymkhana', b'Gymkhana'), (b'techniche', b'Techniche'), (b'technothlon', b'Technothlon'), (b'LS', b'Lecture Series'), (b'SAIL', b'Student Alumni Interaction Linkage (SAIL)'), (b'aeromodelling', b'Aeromodeling Club'), (b'astronomy', b'Astronomy Club'), (b'coding', b'Coding Club'), (b'electronics', b'Electronics Club'), (b'prakriti', b'Prakriti Club'), (b'science', b'Science and Quiz Club'), (b'radioG', b'RadioG'), (b'robotics', b'Robotics Club'), (b'finance', b'Finance and Economics Club'), (b'greenAuto', b'Green Automobile Club'), (b'anchoring', b'Anchoring Club'), (b'cadence', b'Cadence Club'), (b'fineArts', b'Fine Arts Club'), (b'litSoc', b'LitSoc'), (b'movie', b'Movie Club'), (b'music', b'Music Club'), (b'xpressions', b'Xpressions'), (b'montage', b'Montage'), (b'publication', b'Publication Subcommittee'), (b'aquatics', b'Aquatics Club'), (b'athletics', b'Athletics Club'), (b'badminton', b'Badminton Club'), (b'basketball', b'Basketball Club'), (b'cricket', b'Cricket Club'), (b'football', b'Football Club'), (b'hockey', b'Hockey Club'), (b'squash', b'Squash Club'), (b'tableTennis', b'Table Tennis Club'), (b'tennis', b'Tennis Club'), (b'volleyball', b'Volleyball Club'), (b'weightlifting', b'Weightlifting Club'), (b'interaction', b'Interaction Club'), (b'benevolence', b'Benevolence Cell'), (b'social', b'Social Service Club'), (b'advisory', b"Students' Advisory Council"), (b'youth', b'Youth Empowerment Club'), (b'rights', b'Rights & Responsibility Club'), (b'counselling', b'Counselling Cell'), (b'redRibbon', b'Red Ribbon Club'), (b'hostel', b'Hostel Affairs Board'), (b'other', b'Other'), (b'Manthan', b'Manthan'), (b'Kriti', b'Manthan')]),
        ),
        migrations.AlterOrderWithRespectTo(
            name='achievement',
            order_with_respect_to='recent',
        ),
        migrations.AlterOrderWithRespectTo(
            name='post',
            order_with_respect_to='recent',
        ),
    ]
