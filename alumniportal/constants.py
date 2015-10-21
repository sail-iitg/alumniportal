"""
Choices for fields in models.
"""
CLUBS = (
    ('alcheringa', 'Alcheringa'),
    ('EDC', 'Entrepreneurial Development Cell (EDC)'),
    ('gymkhana', 'Gymkhana'),
    ('techniche', 'Techniche'),
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
)
GENDERS = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
)
PROGRAMS = (
    ('b', 'B.Tech.'),
    ('m', 'M.Tech.'),
    ('bd', 'B.Des.'),
    ('p', 'Ph.D.'),
    ('other', 'Other')
)

COMMENCMENT_YEARS = [(i+1994,i+1994) for i in range(37)]
PASS_OUT_YEARS = [(98,1998), (99,1999)] + [(i,i+2000) for i in range(21)]

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
    ('U', 'University'),
    ('A', 'Alumni'),
    ('S', 'Student'),
    ('R', 'Research'),
    )

PROFILE_TYPE = (
    ('is_iitg', 'IITG'),
    ('is_alumni', 'Alumni'),
    ('is_stud', 'Current Student'),
    ('is_prof', 'Professor'),
    )