from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
	name = models.CharField(max_length=64)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Company'
		verbose_name_plural = 'Companies'


class Employee(models.Model):
	user = models.OneToOneField(User)
	company = models.ForeignKey(Company)

	def __str__(self):
		return self.user.username

	class Meta:
		verbose_name = 'Employee'


class AssignedShift(models.Model):
	_DAY_CHOICES = (
		('Monday', 'Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday', 'Wednesday'),
		('Thursday', 'Thursday'),
		('Friday', 'Friday'),
		('Saturday', 'Saturday'),
		('Sunday', 'Sunday')
	)
	
	day = models.CharField(max_length=10, choices=_DAY_CHOICES)
	start_time = models.TimeField()
	end_time = models.TimeField()
	employee = models.ForeignKey(Employee)
	cover_requested = models.BooleanField(default=False)

	def __str__(self):
		return '{0}, {1}-{2} ({3})'.format(
			self.day,
			self.start_time, 
			self.end_time, 
			self.employee.user.username
		)

	class Meta:
		verbose_name = 'Shift'


class PreferredShift(models.Model):
	_DAY_CHOICES = (
		('Monday', 'Monday'),
		('Tuesday', 'Tuesday'),
		('Wednesday', 'Wednesday'),
		('Thursday', 'Thursday'),
		('Friday', 'Friday'),
		('Saturday', 'Saturday'),
		('Sunday', 'Sunday')
	)
	
	day = models.CharField(max_length=10, choices=_DAY_CHOICES)
	start_time = models.TimeField()
	end_time = models.TimeField()
	employee = models.ForeignKey(Employee)

	def __str__(self):
		return '{0}, {1}-{2} ({3})'.format(
			self.day,
			self.start_time, 
			self.end_time, 
			self.employee.user.username
		)

	class Meta:
		verbose_name = 'Preferred Time'
