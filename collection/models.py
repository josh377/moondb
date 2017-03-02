from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count, Q, Sum
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from datetime import datetime, timedelta



class Climb(models.Model):
	GRADES = (
        (13, '8b'),
		(12, '8a+'),
		(11, '8a'),
		(10, '7c+'),
		(9, '7c'),
		(8, '7b+'),
		(7, '7b'),
		(6, '7a+'),
		(5, '7a'),
		(4, '6c+'),
		(3, '6c'),
		(2, '6b+'),
	)
	STARS = (
		(3, '3'),
		(2, '2'),
		(1, '1'),
		(0, '0'),
	)
	name = models.CharField(max_length=255, unique=True)
	grade = models.IntegerField(choices=GRADES)
	stars = models.IntegerField(choices=STARS, null=True)
	global_repeats = models.IntegerField(null=True, default=0)
	slug = models.SlugField(unique=True)
	date = models.DateTimeField(auto_now_add=True)
	canvas = models.BooleanField(default=False)
	users = models.ManyToManyField(User, through='collection.UserLog')
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
		(8, '7b+'),
		(7, '7b'),
		(6, '7a+'),
		(5, '7a'),
		(4, '6c+'),
		(3, '6c'),
		(2, '6b+'),
	)
	STARS = (
		(3, '3'),
		(2, '2'),
		(1, '1'),
		(0, '0'),
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
	personal_grade = models.IntegerField(choices=GRADES, blank=True)
	stars = models.IntegerField(choices=STARS, blank=True)
	comments = models.TextField(blank=True)
	date = models.DateTimeField(blank=True)
	recommended = models.BooleanField(default=False)
	def __str__(self):
		return "%s %s" % (self.user, self.climb)
	

		
@receiver(post_save, sender=UserLog)
def update_sends(sender, **kwargs):
	if kwargs.get('created', False):
		for userdetailsupdate in UserDetails.objects.filter():
			userdetailsupdate.save()
			

	
class UserDetails(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	location = models.CharField(max_length=255, blank=True)
	height = models.CharField(max_length=255, blank=True)
	weight = models.CharField(max_length=255, blank=True)
	ape_index = models.CharField("Ape Index", max_length=255, blank=True)
	moonboardlocation = models.CharField("Moonboard Location", max_length=255, blank=True)
	
	
	
	
		


	
	
