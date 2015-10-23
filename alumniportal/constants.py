from datetime import datetime
"""
Choices for fields in models.
"""
ADMIN_USERNAME = 'admin'
CLUBS = (
    ('alcheringa', 'Alcheringa'),
    ('EDC', 'Entrepreneurial Development Cell (EDC)'),
    ('gymkhana', 'Gymkhana'),
    ('techniche', 'Techniche'),
    ('technothlon', 'Technothlon'),
    ('LS', 'Lecture Series'),
    ('SAIL', 'Student Alumni Interaction Linkage (SAIL)'),

    ('aeromodelling', 'Aeromodeling Club'),
    ('astronomy', 'Astronomy Club'),
    ('coding', 'Coding Club'),
    ('electronics', 'Electronics Club'),
    ('prakriti', 'Prakriti Club'),
    ('science', 'Science and Quiz Club'),
    ('radioG', 'RadioG'),
    ('robotics', 'Robotics Club'),
    ('finance', 'Finance and Economics Club'),
    ('greenAuto', 'Green Automobile Club'),

    ('anchoring', 'Anchoring Club'),
    ('cadence', 'Cadence Club'),
    ('fineArts', 'Fine Arts Club'),
    ('litSoc', 'LitSoc'),
    ('movie', 'Movie Club'),
    ('music', 'Music Club'),
    ('xpressions', 'Xpressions'),
    ('montage', 'Montage'),
    ('publication', 'Publication Subcommittee'),

    ('aquatics', 'Aquatics Club'),
    ('athletics', 'Athletics Club'),
    ('badminton', 'Badminton Club'),
    ('basketball', 'Basketball Club'),
    ('cricket', 'Cricket Club'),
    ('football', 'Football Club'),
    ('hockey', 'Hockey Club'),
    ('squash', 'Squash Club'),
    ('tableTennis', 'Table Tennis Club'),
    ('tennis', 'Tennis Club'),
    ('volleyball', 'Volleyball Club'),
    ('weightlifting', 'Weightlifting Club'),

    ('interaction', 'Interaction Club'),
    ('benevolence', 'Benevolence Cell'),
    ('social', 'Social Service Club'),
    ('advisory', "Students' Advisory Council"),
    ('youth', 'Youth Empowerment Club'),
    ('rights', 'Rights & Responsibility Club'),
    ('counselling', 'Counselling Cell'),
    ('redRibbon', 'Red Ribbon Club'),
    ('hostel', 'Hostel Affairs Board'),
    ('other', 'Other'),

    ('Manthan', 'Manthan'),
    ('Kriti', 'Manthan'),
)
GENDERS = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
)
PROGRAMS = (
    ('B. Tech', 'B.Tech.'),
    ('M. Tech', 'M.Tech.'),
    ('B. Des', 'B.Des.'),
    ('Ph.D.', 'Ph.D.'),
    ('Other', 'Other')
)
MAX_YEAR = datetime.now().year + 4
COMMENCMENT_YEARS = [(i,i) for i in range(1994, MAX_YEAR - 4)]
PASS_OUT_YEARS = []
for i in PROGRAMS:
    for j in range(1998, MAX_YEAR):
        PASS_OUT_YEARS = PASS_OUT_YEARS + [(str(j) + " " + i[1], str(j) + " " + i[1])]
# PASS_OUT_YEARS = [(str(i)+ for j in PROGRAMS, str(i)+ for jjjj in PROGRAMS)   for i in range(1998, MAX_YEAR)]
# PASS_OUT_YEARS = [(1998,'1998-BTec'), (1999,1999)] + [(i+2000,i+2000) for i in range(21)]

DEPARTMENTS = (
    ('bt', 'Biotechnology [BT]'),
    ('cl', 'Chemical [CL]'),
    ('che', 'Chemistry [CHE]'),
    ('ce', 'Civil [CE]'),
    ('cse', 'Computer Science [CSE]'),
    ('ds', 'Design [DD]'),
    ('eee', 'Electrical [EEE]'),
    ('ece', 'Electronics [ECE]'),
    ('hss', 'Humanities &amp; Social Sciences [HSS]'),
    ('ma', 'Mathematics [MA]'),
    ('me', 'Mechanical [ME]'),
    ('ep', 'Physics [EP]'),
    ('cfe', 'Centre for Energy'),
    ('cfte', 'Centre for the Environment'),
    ('cnt', 'Centre for Nanotechnology'),
    ('o', 'Other'),
)

OCCUPATIONS = (
    ('scholar', 'Scholar'),
    ('job', 'Job'),
    ('startup', 'Startup/NGO'),
    ('other', 'Other'),
)

HOSTELS = (
    ('Barak', 'Barak'),
    ('Brahmaputra', 'Brahmaputra'),
    ('Dhansiri', 'Dhansiri'),
    ('Dibang', 'Dibang'),
    ('Dihing', 'Dihing'),
    ('Kameng', 'Kameng'),
    ('Kapili', 'Kapili'),
    ('Lohit', 'Lohit'),
    ('Manas', 'Manas'),
    ("Married Scholar's Hostel", "Married Scholar's Hostel"),
    ('Siang', 'Siang'),
    ('Subansiri', 'Subansiri'),
    ('Umiam', 'Umiam'),
    ('Other', 'Other'),
)

ACTIVITY_TYPE = (
    ('Event', 'Event'),
    ('Meet', 'Alumni Meet'),
    ('Volunteering', 'Start a Volunteering Activity'),
    ('Survey', 'Take a Survey'),
    ('Project', 'Float a Project'),
    )

POST_TYPE = (
    ('I', 'IITG'),
    ('A', 'Alumni'),
    ('S', 'Student'),
    ('R', 'Research'),
    ('B', 'Blog'),
    )

PROFILE_TYPE = (
    ('is_iitg', 'IITG'),
    ('is_alumni', 'Alumni'),
    ('is_stud', 'Current Student'),
    ('is_prof', 'Professor'),
    )

ACHIEVEMENT_TYPE = (
    ('A', 'Alumni'),
    ('I','IITG'),
    ('S', 'Student'),
    )