from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from constants import *
import os
from time import strftime
# from datetime import datetime
# Create your models here.
# mydict = {
#     "Blog" : os.path.join('profile_picture', str(instance.profile.roll_no), filename),
#     "Post" : os.path.join('posts', instance.blog.profile.user.username, instance.timestamp, filename),
#     "Activity" : os.path.join('activity',instance.activity_type, instance.name, str(instance.created), filename),
#     "News"  : os.path.join('news',instance.timestamp, filename),
#     }
# datetime_dir = strftime("%Y%m%d_%H%M%S")
def get_image_path(instance, filename):
    if type(instance).__name__ == "Blog":
        return os.path.join('profile_picture', str(instance.profile.roll_no), filename)
    elif type(instance).__name__ == "Post":
        return os.path.join('posts', instance.blog.profile.user.username, str(instance.timestamp.strftime("%Y%m%d_%H%M%S")), filename)
    elif type(instance).__name__ == "ActivityImage":
        return os.path.join('activity', instance.activity.activity_type, instance.activity.profile.user.username, str(instance.activity.created.strftime("%Y%m%d_%H%M%S")), filename)
    elif type(instance).__name__ == "News":
        return os.path.join('news',str(instance.timestamp.strftime("%Y%m%d_%H%M%S")), filename)

class Profile(models.Model):
    profile_type = models.CharField(max_length=16, choices=PROFILE_TYPE, blank=True)
    # Personal
    user = models.OneToOneField(User, blank=True)  #webmail ID of the person (it acts as the username)
    name = models.CharField(max_length=50)  #Full Name with the designation
    gender = models.CharField(max_length=7, choices=GENDERS, blank=True) #Choices
    date_of_birth = models.DateTimeField(blank=True, null=True)  #Date of Birth
    alternate_email = models.EmailField(blank=True)   #Alternate EmailID (Non IITG)
    hostel = models.CharField(max_length=15, choices=HOSTELS, blank=True)    #Name of the hostel
    room_no = models.CharField(max_length=10, blank=True)    #Room No. of that person while living in IITG
    roll_no = models.IntegerField(unique=True, primary_key=True)    #Row ID of the profiles
    batch = models.CharField(max_length=16, choices=PASS_OUT_YEARS)  #Batch (Pass Out Year) of the person
    department = models.CharField(max_length=25, choices=DEPARTMENTS, blank=True)    #Department in which he was in IITG
    # Contact
    home_contact_no = models.CharField(max_length=15, blank=True)   #Home Contact No.
    work_contact_no = models.CharField(max_length=15, blank=True)   #Work Contact No.
    current_address = models.TextField(blank=True)    #Complete Address
    city = models.CharField(max_length=32, blank=True)  #City currently living in. Useful to filter people on the basis of the city
    country = models.CharField(max_length=32, blank=True)   #Country currently living in. Useful to filter people on the basis of the country
    nationality = models.CharField(max_length=32, blank=True)   #Nationality of the person
    # Social
    google_link = models.URLField(blank=True) #Google Plus Profile link
    linkedin_link = models.URLField(blank=True)   #LinkedIn Profile Link
    facebook_link = models.URLField(blank=True)   #Facebook Profile Link
    github_link = models.URLField(blank=True) #Github Repo Link
    twitter_link = models.URLField(blank=True)    #Twitter Profile Link

    currentJob = models.OneToOneField('Job', blank=True, null=True, related_name='currentJob')   #Row ID of the job object currently doing
    currentEducation = models.OneToOneField('Education', blank=True, null =True, related_name='currentEducation')

    def __unicode__(self):
        return str(self.user.username)


class Blog(models.Model):
    """
    Constantly updating table. Unique to the person. Contains his views, posts, videos and images (s)he uploaded.
    Like a social page.
    """
    # profile_id = models.IntegerField(unique=True, primary_key=True) #Unique to the person
    profile = models.OneToOneField('Profile', blank=True)  #Row ID of Blog Class
    # TODO: Shift profile_picture to Profile model instead of Blog
    profile_picture = models.ImageField(blank=True, null=True, upload_to=get_image_path)   #Profile Picture of the person
    videos = models.TextField(blank=True) #List of path to the videos that the person with profile_id = roll_no has uploaded
    # posts = models.TextField(blank=True)      #List of lists. [["TimeStamp", "Header of Post", "Content"]]. It will be updated from the end.
    about_me = models.TextField(blank=True)   #About me
    interests = models.TextField(blank=True)  #Interests/Hobbies
    message_to_the_world = models.TextField(blank=True)   #What the person wants to say to the world
    images = models.TextField(blank=True) #List of path to the images that the person with profile_id = roll_no has uploaded

    def __unicode__(self):
        return str(self.profile.user.username)


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

    class Meta:
        ordering = ['-week']
        # order_with_respect_to = 'week'

    def __unicode__(self):
        return self.week

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

    class Meta:
        ordering = ['-year']
        # order_with_respect_to = 'recent'

class Education(models.Model):
    """
    Degree of an alumnus in and outside IITG
    """
    profile = models.ForeignKey(Profile, blank=True, related_name='educations')  #roll_no referring to the person to which the education object belongs
    degree = models.CharField(max_length=40, choices=PROGRAMS)  #Name of the degree
    institute = models.CharField(max_length=100)
    start_year = models.IntegerField(null=True) #Start Year of the education
    end_year = models.IntegerField(blank=True, null=True)   #PassOut Year of the education
    department = models.CharField(max_length=50, choices=DEPARTMENTS) #
    specialization = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
        return str(self.institute)

class Job(models.Model):
    """Past job of an alumnus"""
    profile = models.ForeignKey(Profile, blank=True, related_name='jobs')
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50, blank=True)
    start_date = models.IntegerField(choices=COMMENCMENT_YEARS)
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
    image = models.ImageField(upload_to=get_image_path)
    created = models.DateTimeField(blank=True)   #Date and time of the start of the activity (Could be timestamp for some)
    end_date = models.DateTimeField(blank=True, null=True)   #
    requirement = models.TextField(blank=True)    #Requirements if any
    description = models.TextField(blank=True)    #Short summary of the activity. How to be performed etc
    peoples_involved = models.ManyToManyField(Profile, blank=True)   #No. of peoples currently got involved.
    recent = models.ForeignKey(Recent, blank=True, null=True, related_name='activities')
    status = models.CharField(max_length=16, choices = STATUS)

    def __unicode__(self):
        return str(self.created)

    class Meta:
        ordering = ['-created']
        # order_with_respect_to = 'recent'
class ActivityImage(models.Model):
    activity = models.ForeignKey(Activity, related_name='images')
    image = models.ImageField(upload_to=get_image_path)

class Club(models.Model):
    name = models.CharField(max_length=32)  #Name of the club
    description = models.TextField()    #Descripton of the club
    members = models.ManyToManyField(Profile, blank=True)    #List of the profile_id of the cluv

class ClubPost(models.Model):
    member = models.ForeignKey(Profile, blank=True, related_name='clubposts')
    heading = models.CharField(max_length=64)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    club = models.ForeignKey(Club, related_name='club')
    # image = models.ImageField(blank=True, null=True, upload_to = get_image_path)

class News(models.Model):
    post_type = models.CharField(max_length=2, choices = POST_TYPE) #Will only be visible in custom form to Admin users only. (For Now)
    timestamp = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=128)
    content = RichTextField()
    image = models.ImageField(blank=True, null=True, upload_to=get_image_path)  #Currently just one
    recent = models.ForeignKey(Recent, null=True, blank=True, related_name='news')

    class Meta:
        ordering = ['-timestamp']
        # order_with_respect_to = 'recent'
    def __unicode__(self):
        return str(self.post_type + " " + str(self.timestamp))

class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images')
    image = models.ImageField(upload_to=get_image_path)

class Post(models.Model):
    """
    Denotes a General Class for News and Blog posts.
    Admin if uses post_type other than 'B' are considered as news. 'R' categorised as Research News and so on.
    If post_type = 'B' then they re individual BLOGS.
    """
    blog = models.ForeignKey(Blog)
    timestamp = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=128)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to=get_image_path)
    recent = models.ForeignKey(Recent, null=True, blank=True, related_name='posts')

    class Meta:
        ordering = ['-timestamp']
        # order_with_respect_to = 'recent'
    def __unicode__(self):
        return str(self.blog.profile.name + " " + str(self.timestamp))


class PostComment(models.Model):
    """
    Comment on a blog post
    """
    author = models.ForeignKey(Profile, blank=True, null=True)
    comment = models.CharField(max_length = 1500)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)

    def __unicode__(self):
        dt = self.post.timestamp
        return '%s %s-%s-%s %02d:%d %s...' % (self.post.blog.profile.name,
            dt.year, dt.month, dt.day, dt.hour, dt.minute, self.comment[:20])
