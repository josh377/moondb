from django.db import models
from django.contrib.auth.models import User

class Climb(models.Model):
	GRADES = (
        (13, '8b'),
		(12, '8a+'),
		(11, '8a'),
		(10, '7c+'),
		(9, '7c'),
		(8.25, '7b+'),
		(7.75, '7b'),
		(7, '7a+'),
		(6, '7a'),
		(5, '6c+'),
		(4, '6c'),
		(3, '6b+'),
	)
	STARS = (
		('3', '3'),
		('2', '2'),
		('1', '1'),
		('0', '0'),
	)
	name = models.CharField(max_length=255, unique=True)
	grade = models.IntegerField(choices=GRADES)
	stars = models.CharField(max_length=255, choices=STARS, blank=True)
	global_repeats = models.CharField(max_length=255, blank=True)
	slug = models.SlugField(unique=True)
	date = models.DateTimeField(auto_now_add=True)
	canvas = models.BooleanField(default=False)
	def __str__(self):
		return '%s %s' % (self.name, self.get_grade_display())

	
class Video(models.Model):
	climb = models.ForeignKey(Climb, on_delete=models.CASCADE)
	url = models.CharField(max_length=9999)
	uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "%s" % (self.climb)
	

class UserLog(models.Model):
	GRADES = (
        (13, '8b'),
		(12, '8a+'),
		(11, '8a'),
		(10, '7c+'),
		(9, '7c'),
		(8.25, '7b+'),
		(7.75, '7b'),
		(7, '7a+'),
		(6, '7a'),
		(5, '6c+'),
		(4, '6c'),
		(3, '6b+'),
	)
	STARS = (
		('3', '3'),
		('2', '2'),
		('1', '1'),
		('0', '0'),
	)
	ATTEMPTS = (
		('More than 3', 'More than 3'),
		('3rd Go', '3rd Go'),
		('2nd Go', '2nd Go'),
		('Flash', 'Flash'),
	)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	climb = models.ForeignKey(Climb, on_delete=models.CASCADE)
	attempts = models.CharField(max_length=255, choices=ATTEMPTS, blank=True)
	personal_grade = models.IntegerField(choices=GRADES)
	stars = models.CharField(max_length=255, choices=STARS)
	comments = models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "%s %s" % (self.user, self.climb)
	