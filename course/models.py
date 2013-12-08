from datetime import datetime

from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModel

class Course(TimeStampedModel):
	name = models.CharField(max_length=256)
	last_date = models.DateField(blank=True)
	owner = models.ForeignKey(User)

	def __unicode__(self):
		return self.name

class Deadline(TimeStampedModel):
	name = models.CharField(max_length=256)
	course = models.ForeignKey(Course)
	date_due = models.DateField(blank=True)
	maker = models.ForeignKey(User)

	def __unicode__(self):
		return self.name

	def __lt__(self, other):
		return self.date_due < other.date_due


class Group(TimeStampedModel):
	name = models.CharField(max_length=256)
	description = models.CharField(max_length=300)

class Update(TimeStampedModel):
	text = models.CharField(max_length=256)
	user = models.ForeignKey(User)
	course = models.ForeignKey(Course, blank=True)
	group = models.ForeignKey(Group, blank=True)

class GroupMember(TimeStampedModel):
	group = models.ForeignKey(Group)
	user = models.ForeignKey(User)

class CourseMember(TimeStampedModel):
	course = models.ForeignKey(Course)
	user = models.ForeignKey(User)
