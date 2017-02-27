from django.forms import ModelForm
from collection.models import Climb, UserLog, Video, UserDetails, User
from django import forms
from django.utils.text import slugify



class NewClimb(forms.ModelForm):
	class Meta:
		model = Climb
		fields = ('name', 'grade')
	def save(self):
		instance = super(NewClimb, self).save(commit=False)
		instance.slug = slugify (instance.name)
		instance.save()
		
		return instance
		
class LogClimb(forms.ModelForm):
	class Meta:
		model = UserLog
		fields = ('climb', 'date', 'attempts', 'personal_grade', 'stars', 'recommended', 'comments')
	def __init__(self, *args, **kwargs):
		super(LogClimb, self).__init__(*args, **kwargs)   
		self.fields['climb'].queryset = Climb.objects.order_by('name')
		
class EditSend(ModelForm):
	class Meta:
		model = UserLog
		fields = ('climb', 'attempts', 'date', 'personal_grade', 'stars', 'recommended', 'comments')
		

class AddVideo(forms.ModelForm):
	class Meta:
		model = Video
		fields = ('climb', 'url',)
	def __init__(self, *args, **kwargs):
		super(AddVideo, self).__init__(*args, **kwargs)   
		self.fields['climb'].queryset = Climb.objects.order_by('name')	
		
class EditClimb(ModelForm):
	class Meta:
		model = Climb
		fields = ('name', 'grade', 'stars', 'global_repeats')
		
		
class EditUserDetails(ModelForm):
	class Meta:
		model = UserDetails
		fields = ('first_name', 'last_name', 'location', 'height', 'weight', 'ape_index', 'moonboardlocation')
		



		


		
		


