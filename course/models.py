from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel

class Course(TimeStampedModel):
	name = models.CharField(max_length=256)
	last_date = models.DateField(blank=True)
	owner = models.ForeignKey(User)

class Assignment(TimeStampedModel):
	name = models.CharField(max_length=256)
	date_due = models.DateField(blank=True)
	maker = models.ForeignKey(User)

class Group(TimeStampedModel):
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=300)

class Update(TimeStampedModel):
	text = models.CharField(max_length=256)
	user = models.ForeignKey(User)

class GroupMembers(TimeStampedModel):
	group = models.ForeignKey(Group)
	user = models.ForeignKey(User)

class CourseMembers(TimeStampedModel):
	course = models.ForeignKey(Course)
	user = models.ForeignKey(User)
