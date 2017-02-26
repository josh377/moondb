from django.contrib import admin
from collection.models import Climb, Video, UserLog, UserDetails
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

class ClimbAdmin(admin.ModelAdmin):
    model = Climb
    list_display = ('name', 'grade', 'canvas', 'stars', 'date')
    prepopulated_fields = {'slug': ('name',)}
	
admin.site.register(Climb, ClimbAdmin)

class VideoAdmin(admin.ModelAdmin):
	model = Video
	list_display = ('climb', 'url', 'uploaded_by', 'date')
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "climb":
			kwargs["queryset"] = Climb.objects.order_by('name')
		return super(VideoAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
admin.site.register(Video, VideoAdmin)

class UserLogAdmin(admin.ModelAdmin):
	model = UserLog
	list_display = ('user', 'climb')
	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == "climb":
			kwargs["queryset"] = Climb.objects.order_by('name')
		return super(UserLogAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)
	
admin.site.register(UserLog, UserLogAdmin)


class UserDetailsInline(admin.StackedInline):
    model = UserDetails
    can_delete = False
    verbose_name_plural = 'userdetails'

class UserAdmin(BaseUserAdmin):
    inlines = (UserDetailsInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)