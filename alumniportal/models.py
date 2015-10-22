from django.db import models
from django.contrib.auth.models import User
from constants import *
import os
# Create your models here.
def get_image_path(instance, filename):
    if type(instance).__name__ == "Blog":
        return os.path.join('profile_picture', str(instance.profile.roll_no), filename)
    elif type(instance).__name__ == "Post":
        if instance.blog.profile.user.username == "admin":
            return os.path.join('news', filename)
        else:
            #####Check for changing the filename before uploading and also about shwing timestamps for different post instances. 
            return os.path.join('posts', instance.blog.profile.user.username, filename)

class Profile(models.Model):
    profile_type = models.CharField(max_length=16, choices=PROFILE_TYPE, blank=True)
    user = models.OneToOneField(User, blank=True)  #webmail ID of the person (it acts as the username)
    roll_no = models.IntegerField(unique=True, primary_key=True)    #Row ID of the profiles
    name = models.CharField(max_length=50, blank=True)  #Full Name with the designation
    gender = models.CharField(max_length=7, choices=GENDERS, blank=True) #Choices
    date_of_birth = models.DateField(blank=True, null=True)  #Date of Birth
    current_job = models.OneToOneField('Job', blank=True, null=True, related_name='current_job')   #Row ID of the job object currently doing
    current_education = models.OneToOneField('Education', blank=True, null =True, related_name='current_education')
    # past_jobs_id = models.TextField()   #List of Row IDs of the job objects
    current_address = models.TextField(blank=True)    #Complete Address
    city = models.CharField(max_length=32, blank=True)  #City currently living in. Useful to filter people on the basis of the city
    country = models.CharField(max_length=32, blank=True)   #Country currently living in. Useful to filter people on the basis of the country 
    nationality = models.CharField(max_length=32, blank=True)   #Nationality of the person
    alternate_email = models.EmailField(blank=True)   #Alternate EmailID (Non IITG)
    # IITG_degrees_id = models.TextField()    #List of education objects with in_iitg=True and profile_id = self.roll_no
    # NonIITG_degrees_id = models.TextField() #List of education objects with in_iitg=False and profile_id = self.roll_no
    google_link = models.URLField(blank=True) #Google Plus Profile link
    linkedin_link = models.URLField(blank=True)   #LinkedIn Profile Link
    facebook_link = models.URLField(blank=True)   #Facebook Profile Link
    github_link = models.URLField(blank=True) #Github Repo Link
    twitter_link = models.URLField(blank=True)    #Twitter Profile Link
    home_contact_no = models.CharField(max_length=15, blank=True)   #Home Contact No.
    work_contact_no = models.CharField(max_length=15, blank=True)   #Work Contact No.
    # projects_id = models.TextField()    #List of Project IDs that the person has done
    # achievements_id = models.TextField()    #List of Achievement IDs for that person
    # IITG_experiences_id = models.TextField()    #List of Experience IDs for that person
    hostel = models.CharField(max_length=15, choices=HOSTELS, blank=True)    #Name of the hostel
    room_no = models.CharField(max_length=10, blank=True)    #Room No. of that person while living in IITG
    batch = models.CharField(max_length=16, choices=PASS_OUT_YEARS)  #Batch (Pass Out Year) of the person
    department = models.CharField(max_length=25, choices=DEPARTMENTS, blank=True)    #Department in which he was in IITG

    def __unicode__(self):
        return str(self.name)

class Blog(models.Model):
    """
    Constantly updating table. Unique to the person. Contains his views, posts, videos and images (s)he uploaded.
    Like a social page.
    """
    # profile_id = models.IntegerField(unique=True, primary_key=True) #Unique to the person
    profile = models.OneToOneField('Profile', blank=True)  #Row ID of Blog Class
    profile_picture = models.ImageField(blank=True, null=True, upload_to=get_image_path)   #Profile Picture of the person
    videos = models.TextField(blank=True) #List of path to the videos that the person with profile_id = roll_no has uploaded
    # posts = models.TextField(blank=True)      #List of lists. [["TimeStamp", "Header of Post", "Content"]]. It will be updated from the end. 
    about_me = models.TextField(blank=True)   #About me
    interests = models.TextField(blank=True)  #Interests/Hobbies
    message_to_the_world = models.TextField(blank=True)   #What the person wants to say to the world
    images = models.TextField(blank=True) #List of path to the images that the person with profile_id = roll_no has uploaded

class IITGExperience(models.Model):
    """
    Activity of an alumnus in institute clubs
    """
    profile = models.ForeignKey(Profile, blank=True, related_name='iitgexperiences')  #roll_no of the person to which the IITGExperience object belongs
    club_name = models.CharField(max_length=30, choices=CLUBS)   #Club about which experience is shared
    experience = models.TextField() #experience shared

    def __unicode__(self):
        return str(self.club_name)

class Recent(models.Model):
    """
    Each row will contain weekly news
    """
    week = models.CharField(primary_key=True, unique = True, max_length=6) #WeekNo padded in two digits concatenated with four digits year
    # news = models.TextField(blank=True)   #List of lists [["timestamp, heading, content"]]
    # posts = models.TextField()  #List of lists [["timestamp, profile_id, heading, content"]]
    # achievements = models.TextField()   #List of lists [["timestamp, achievement_id"]]
    # projects = models.TextField()   #List of lists [["timestamp, project_id"]]
    # activities = models.TextField() #List of lists [["timestamp, activity_id"]]

class Achievement(models.Model):
    """
    Achievements received in or out the campus
    """
    profile = models.ForeignKey(Profile, blank=True, related_name='achievements')  #roll_no referring to the person to which the achievement belongs
    achievement_type = models.CharField(max_length=2, choices=ACHIEVEMENT_TYPE)
    year = models.IntegerField(blank=True, null=True)    #Year of which achievement
    achievement = models.CharField(max_length=128)  #What is the achievement?
    description = models.TextField(blank=True)    #Description about it or experience.
    recent = models.ForeignKey(Recent, blank=True, related_name = 'achievements')

    def __unicode__(self):
        return str(self.achievement)

class Education(models.Model):
    """
    Degree of an alumnus in and outside IITG
    """
    profile = models.ForeignKey(Profile, blank=True, related_name='educations')  #roll_no referring to the person to which the education object belongs
    degree = models.CharField(max_length=40, choices=PROGRAMS)  #Name of the degree
    institute = models.CharField(max_length=100)    #Name of the institute
    in_iitg = models.BooleanField() #Whether it is IITG or not. Used in filling the NonIITG_degrees and IITG_degrees in the Profile Class object.
    start_year = models.IntegerField(null=True) #Start Year of the education
    end_year = models.IntegerField(null=True)   #PassOut Year of the education
    department = models.CharField(max_length=50, choices=DEPARTMENTS) #
    specialization = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return str(self.institute)

class Job(models.Model):
    """Past job of an alumnus"""
    profile = models.ForeignKey(Profile, blank=True, related_name='jobs')
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True)
    start_date = models.IntegerField(blank=True, null=True, choices=COMMENCMENT_YEARS)
    end_date = models.IntegerField(blank=True, null=True, choices=COMMENCMENT_YEARS)
    description = models.CharField(max_length=50, blank=True)
    # occupation = models.CharField(max_length=50, null=True, choices=OCCUPATIONS)
    city = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return str(self.company)

class Project(models.Model):
    """
    Research project that the alumni has done
    """
    profile = models.ForeignKey(Profile, blank=True, related_name='projects')
    topic = models.CharField(max_length=128)
    mentor = models.CharField(max_length=32, blank=True)
    description = models.TextField(blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    recent = models.ForeignKey(Recent, blank=True, related_name='projects')

class Activity(models.Model):
    """
    Includes volunteering activities as well as any meet or event, survey, project floated.
    """
    profile = models.ForeignKey(Profile, related_name='activities', blank=True)
    activity_type = models.CharField(max_length=32, choices=ACTIVITY_TYPE)
    name = models.CharField(max_length=32)  #Name of the Voluteer Activity being proposed
    purpose = models.CharField(max_length=128)  #Purpose of the activity eg. Welfare of society, CrowdSourcing, Survey

    created = models.DateTimeField(blank=True)   #Date and time of the start of the activity (Could be timestamp for some)
    end_date = models.DateTimeField(blank=True, null=True)   #
    requirement = models.TextField(blank=True)    #Requirements if any
    description = models.TextField(blank=True)    #Short summary of the activity. How to be performed etc
    peoples_involved = models.ManyToManyField(Profile, blank=True)   #No. of peoples currently got involved. 
    # peoples_id = models.TextField() #List of the peoples who gor involved
    images = models.TextField(blank=True) #List of the paths of the images which are involved with the activity
    recent = models.ForeignKey(Recent, blank=True, related_name='activities')


class Club(models.Model):
    name = models.CharField(max_length=32)  #Name of the club
    description = models.TextField()    #Descripton of the club
    members = models.ManyToManyField(Profile, blank=True)    #List of the profile_id of the cluv
    posts = models.TextField()  #list of lists in which sublist ["date", "rollno", "content"]

class Post(models.Model):
    blog = models.ForeignKey(Blog)
    post_type = models.CharField(max_length=2, choices = POST_TYPE) #Will only be visible in custom form to Admin users only. (For Now)
    timestamp = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=get_image_path)
    recent = models.ForeignKey(Recent, blank=True, related_name='posts')
