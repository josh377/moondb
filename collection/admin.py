from django.contrib import admin
from collection.models import Climb, Video, UserLog

class ClimbAdmin(admin.ModelAdmin):
    model = Climb
    list_display = ('name', 'grade', 'stars', 'global_repeats', 'date')
    prepopulated_fields = {'slug': ('name',)}
	
admin.site.register(Climb, ClimbAdmin)

class VideoAdmin(admin.ModelAdmin):
	model = Video
	list_display = ('climb', 'url', 'uploaded_by', 'date')
	
admin.site.register(Video, VideoAdmin)

class UserLogAdmin(admin.ModelAdmin):
	model = UserLog
	list_display = ('user', 'climb', 'date')
	
admin.site.register(UserLog, UserLogAdmin)