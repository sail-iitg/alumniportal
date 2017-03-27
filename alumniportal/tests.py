from django.test import TestCase
from alumniportal import models
from django.contrib.auth.models import User
from django.db import transaction
from django.db import IntegrityError
import csv


efp = open('../error.csv','w')
repeatfp = open('../repeat.csv','w')
with open('../2001_2015.csv','r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    with transaction.atomic():
        for row in reader:
            if(row[0] == '' or row[1] == '' or row[2] == ''):
                efp.write(",".join(row) + "\n")
            else:
                if len(User.objects.filter(username = row[2])) == 0:
                    user = User.objects.create_user(username = row[2], password = row[2])
                    models.Profile.objects.create(roll_no = row[0], user = user, name = row[1]).save()
                else:
                    repeatfp.write(",".join(row) + "\n")
