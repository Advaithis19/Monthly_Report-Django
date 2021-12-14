from typing import Callable
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.constraints import UniqueConstraint
from django.db.models.deletion import CASCADE
from django.db.models.fields import NullBooleanField
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

usermodel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(usermodel, null=True, on_delete=CASCADE)

    fname = models.CharField(max_length=50, null=True)
    mname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)

    uname = models.CharField(max_length=50, null=True)


    AEROSPACE = 'AE'
    BIOTECH = 'BT'
    CHEMICAL = 'CE'
    CIVIL = 'CE'
    COMPUTERSC = 'CSE'
    ELECTRICAL = 'EEE'
    ELECTRONICSCM = 'ECE'
    ELECTRONICSIN = 'EIE'
    INDUSTRIAL = 'IEM'
    INFORMATIONSC = 'ISE'
    MASTERCA = 'MCA'
    MECHANICAL = 'ME'
    ELECTRONICSTE = 'ETE'
    BASICSC = 'BSC'

    DEPARTMENT = [
        (AEROSPACE, 'Aerospace Engineering'),
        (BIOTECH, 'Biotechnology'),
        (CHEMICAL, 'Chemical Engineering'),
        (CIVIL, 'Civil Engineering'),
        (COMPUTERSC, 'Computer Science and Engineering'),
        (ELECTRICAL, 'Electrical and Electronics Engineering'),
        (ELECTRONICSCM, 'Electronics and Communication Engineering'),
        (ELECTRONICSIN, 'Electronics and Instrumentation Engineering'),
        (INDUSTRIAL, 'Industrial Engineering and Management'),
        (INFORMATIONSC, 'Information Science and Engineering'),
        (MASTERCA, 'Master of Computer Applications'),
        (MECHANICAL, 'Mechanical Engineering'),
        (ELECTRONICSTE, 'Electronics and Telecommunication Engineering (Telecommunication Engineering)'),
        (BASICSC, 'Basic Sciences'),
        
    ]

    department = models.CharField(
        max_length=3,
        choices=DEPARTMENT,
        default=INFORMATIONSC,
    )

    def __str__(self):
        return self.fname or ""

class Grants(models.Model):
    title = models.CharField(max_length=50)
    agency = models.CharField(max_length=50)
    sanc_amt = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField(default = 2022, null=False)
    remarks = models.CharField(max_length=50, null = True)
    date_added = models.DateField(default=timezone.now())

    PI = models.ForeignKey(Profile, on_delete=CASCADE, related_name='grants_prinvestigated', null=True)
    CO_PI = models.ForeignKey(Profile, on_delete=CASCADE, related_name='grants_coprinvestigated', null=True)

    UniqueConstraint(fields=['title', 'PI', 'CO_PI'], name='unique_grant')

    def __str__(self):
        return self.title

class Proposal(models.Model):
    title = models.CharField(primary_key=True, max_length=50)
    submitted_to = models.CharField(max_length=50)
    budg_amt = models.DecimalField(max_digits=6, decimal_places=2)

    ACCEPT = 'AC'
    REJECT = 'RE'
    ONGOING = 'ON' 

    status_list = [
        (ACCEPT, 'Accepted'),
        (REJECT, 'Rejected'),
        (ONGOING, 'Ongoing'),
    ]

    status = models.CharField(
        max_length=3,
        choices=status_list,
        null=True,
    )

    date_added = models.DateField(default=timezone.now())

    def __str__(self):
        return self.title

    PI = models.ForeignKey(Profile, on_delete=CASCADE, related_name='proposals_prinvestigated', null=True)
    CO_PI = models.ForeignKey(Profile, on_delete=CASCADE, related_name='proposals_coprinvestigated', null=True)

    UniqueConstraint(fields=['title', 'PI', 'CO_PI'], name='unique_grant')

class Consultancy(models.Model):
    title = models.CharField(max_length=50)
    fund_agency = models.CharField(max_length=50)
    rec_amt = models.DecimalField(max_digits=6, decimal_places=2)
    date_added = models.DateField(default=timezone.now())

    f_id = models.ForeignKey(Profile, on_delete=CASCADE)
    UniqueConstraint(fields=['title', 'f_id'], name='unique_consultancy') 

    def __str__(self):
        return self.title

class Workshop(models.Model):
    event_name = models.CharField(primary_key=True, max_length=50)
    venue = models.CharField(max_length=100)
    date = models.DateField()
    date_added = models.DateField(default=timezone.now())

    u_id = models.ManyToManyField(Profile)

    def __str__(self):
        return self.event_name

class Lecture(models.Model):
    topic = models.CharField(max_length=50)
    res_person = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    n_stud = models.IntegerField(null=True)
    n_fac = models.IntegerField(null=True)
    n_ind = models.IntegerField(null=True)
    date_added = models.DateField(default=timezone.now())

    f_id = models.ForeignKey(Profile, on_delete=CASCADE)
    UniqueConstraint(fields=['topic', 'f_id'], name='unique_lecture')

    def __str__(self):
        return self.topic

class Event(models.Model):
    title = models.CharField(primary_key=True, max_length=50)
    venue = models.CharField(max_length=100)
    date_added = models.DateField()
    n_stud = models.IntegerField(null=True)
    n_fac = models.IntegerField(null=True)
    n_ind = models.IntegerField(null=True)
    date = models.DateField()
    date_added = models.DateField(default=timezone.now())

    u_id = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title

class Talk(models.Model):
    topic = models.CharField(max_length=50)
    venue = models.CharField(max_length=100)
    n_stud = models.IntegerField(null=True)
    n_fac = models.IntegerField(null=True)
    n_ind = models.IntegerField(null=True)
    date = models.DateField()
    date_added = models.DateField(default=timezone.now())

    f_id = models.ForeignKey(Profile, on_delete=CASCADE)
    UniqueConstraint(fields=['topic', 'f_id'], name='unique_talk')

    def __str__(self):
        return self.topic

class Other_Activity(models.Model):
    act_id = models.IntegerField()
    activity = models.CharField(max_length=100)
    date = models.DateField()
    date_added = models.DateField(default=timezone.now())

    f_id = models.ForeignKey(Profile, on_delete=CASCADE)
    UniqueConstraint(fields=['act_id', 'f_id'], name='unique_activity')

    def __str__(self):
        return self.activity

class Achievement(models.Model):
    title = models.CharField(max_length=50)
    organisation = models.CharField(max_length=50)
    date_added = models.DateField(default=timezone.now())

    f_id = models.ForeignKey(Profile, on_delete=CASCADE)
    UniqueConstraint(fields=['title', 'f_id'], name='unique_achievement')

    def __str__(self):
        return self.title

class Conference(models.Model):
    title = models.CharField(primary_key=True, max_length=50)
    conference = models.CharField(max_length=100)
    volume = models.IntegerField()
    issue = models.IntegerField()
    n_page = models.IntegerField()

    NATIONAL = 'NAT'
    INTERNATIONAL = 'INT' 

    choice_list = [
        (NATIONAL, 'National'),
        (INTERNATIONAL, 'International'),
    ]

    nat_int = models.CharField(
        max_length=3,
        choices=choice_list,
        null=True
    )
    date_added = models.DateField(default=timezone.now())

    u_id = models.ForeignKey(Profile, on_delete=CASCADE)

    def __str__(self):
        return self.title

    

class MoU(models.Model):
    organisation = models.CharField(primary_key=True, max_length=50)
    mod_col = models.CharField(max_length=25)
    date_added = models.DateField()
    validity = models.IntegerField()
    date = models.DateField()
    date_added = models.DateField(default=timezone.now())

    u_id = models.ManyToManyField(Profile)

    def __str__(self):
        return self.organisation

class Patent(models.Model):
    title = models.CharField(primary_key=True, max_length=50)
    topic = models.CharField(max_length=50)

    ACCEPT = 'AC'
    REJECT = 'RE'
    ONGOING = 'ON' 

    status_list = [
        (ACCEPT, 'Accepted'),
        (REJECT, 'Rejected'),
        (ONGOING, 'Ongoing'),
    ]

    status = models.CharField(
        max_length=3,
        choices=status_list,
        null=True,
    )
    date_added = models.DateField(default=timezone.now())

    u_id = models.ManyToManyField(Profile)

    def __str__(self):
        return self.title

class Industrial_visit(models.Model):
    visit_no = models.IntegerField(primary_key=True)
    purpose = models.CharField(max_length=100)
    industry = models.CharField(max_length=50)
    semester = models.IntegerField(
        validators=[
            MaxValueValidator(8),
            MinValueValidator(1)
        ]
    )
    n_stud = models.IntegerField(null=True)
    date_added = models.DateField(default=timezone.now())

    u_id = models.ManyToManyField(Profile)

    def __str__(self):
        return self.industry

class Membership(models.Model):
    mem_id = models.IntegerField(primary_key=True)
    membership = models.CharField(max_length=50)
    association = models.CharField(max_length=50)
    term=models.IntegerField(null=True)
    date_added = models.DateField(default=timezone.now())

    u_id = models.ManyToManyField(Profile)

    def __str__(self):
        return self.membership

class Book(models.Model):
    n_isbn = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    date_added = models.DateField(default=timezone.now())

    u_id = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name























