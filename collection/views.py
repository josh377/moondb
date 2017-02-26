from django.shortcuts import render, redirect, reverse
from collection.models import Climb, Video, UserLog
from django.db.models import Count, Avg, Sum
from collection.forms import NewClimb, LogClimb, AddVideo
from django.contrib.auth.models import User
from datetime import datetime, timedelta


def home(request):
	recent_sends = UserLog.objects.order_by('-date')
	recent_videos = Video.objects.order_by('-date')
	return render(request, 'index.html', {
		'recent_sends': recent_sends,
		'recent_videos': recent_videos,
		
})


def climb_detail(request, slug):
	climb = Climb.objects.get(slug=slug)
	video = Video.objects.filter(climb__slug=slug)
	videocount = Video.objects.filter(climb__slug=slug).count()
	log = UserLog.objects.filter(climb__slug=slug)
	localstars = UserLog.objects.filter(climb__slug=slug).aggregate(Avg('stars'))
	localgrade = UserLog.objects.filter(climb__slug=slug).aggregate(Avg('personal_grade'))
	localsends = UserLog.objects.filter(climb__slug=slug).count()
	return render(request, 'climbs/climb_detail.html', {
		'localstars': localstars,
		'localsends': localsends,
		'localgrade': localgrade,
        'climb': climb,
		'video': video,
		'log': log,
		'videocount': videocount,
})

def climb_detail_condensed(request, slug):
	climb = Climb.objects.get(slug=slug)
	video = Video.objects.filter(climb__slug=slug)
	videocount = Video.objects.filter(climb__slug=slug).count()
	log = UserLog.objects.filter(climb__slug=slug)
	localstars = UserLog.objects.filter(climb__slug=slug).aggregate(Avg('stars'))
	localgrade = UserLog.objects.filter(climb__slug=slug).aggregate(Avg('personal_grade'))
	localsends = UserLog.objects.filter(climb__slug=slug).count()
	return render(request, 'climbs/condensed/climb_detail_condensed.html', {
		'localstars': localstars,
		'localsends': localsends,
		'localgrade': localgrade,
        'climb': climb,
		'video': video,
		'log': log,
		'videocount': videocount,
})



def new_climb(request):
	if request.method == "POST":
		form = NewClimb(request.POST)
		if form.is_valid():
			
			climb = form.save()
			return redirect(reverse('climb_detail', kwargs={'slug': climb.slug})
			)
	else:
		form = NewClimb()
	return render(request, 'new_climb.html', {'form': form})
	


def log_climb(request):
	if request.method == "POST":
		form = LogClimb(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			userid = request.user
			obj.user = request.user
			obj.save()
			return redirect('user_profile', uid=userid.id)
	else:
		form = LogClimb()
	return render(request, 'log_climb.html', {'form': form})
	
	
def add_video(request):
	if request.method == "POST":
		form = AddVideo(request.POST)
		if form.is_valid():
			obj = form.save(commit=False)
			obj.uploaded_by = request.user
			obj.save()
			video = form.save()
			return redirect('climb_detail', slug=video.climb.slug)
	else: 
		form = AddVideo()
	return render(request, 'add_video.html', {'form': form})
	

def user_profile(request, uid):
	profile = User.objects.get(id=uid)
	log = UserLog.objects.filter(user__id=uid).order_by('personal_grade', 'date')
	totalsends = UserLog.objects.filter(user__id=uid).count()
	totalvpoints = UserLog.objects.filter(user__id=uid).aggregate(Sum('personal_grade'))
	this_month = datetime.now().month
	thismonthcount = UserLog.objects.filter(user__id=uid, date__month=this_month).count()
	thismonthpoints = UserLog.objects.filter(user__id=uid, date__month=this_month).aggregate(Sum('personal_grade'))
	sends8b = UserLog.objects.filter(user__id=uid, personal_grade=13).count()
	sends8aplus = UserLog.objects.filter(user__id=uid, personal_grade=12).count()
	sends8a = UserLog.objects.filter(user__id=uid, personal_grade=11).count()
	sends7cplus = UserLog.objects.filter(user__id=uid, personal_grade=10).count()
	sends7c = UserLog.objects.filter(user__id=uid, personal_grade=9).count()
	sends7bplus = UserLog.objects.filter(user__id=uid, personal_grade=8.25).count()
	sends7b = UserLog.objects.filter(user__id=uid, personal_grade=7.75).count()
	sends7aplus = UserLog.objects.filter(user__id=uid, personal_grade=7).count()
	sends7a = UserLog.objects.filter(user__id=uid, personal_grade=6).count()
	sends6cplus = UserLog.objects.filter(user__id=uid, personal_grade=5).count()
	sends6c = UserLog.objects.filter(user__id=uid, personal_grade=4).count()
	sends6bplus = UserLog.objects.filter(user__id=uid, personal_grade=3).count()
	videosadded = Video.objects.filter(uploaded_by__id=uid).count()
	return render(request, 'users/user_profile.html', {
		'profile': profile,
		'log': log,
		'totalsends': totalsends,
		'totalvpoints': totalvpoints,
		'thismonthcount': thismonthcount,
		'thismonthpoints': thismonthpoints,
		'sends8b': sends8b,
		'sends8aplus': sends8aplus,
		'sends8a': sends8a,
		'sends7cplus': sends7cplus,
		'sends7c': sends7c,
		'sends7bplus': sends7bplus,
		'sends7b': sends7b,
		'sends7aplus': sends7aplus,
		'sends7a': sends7a,
		'sends6cplus': sends6cplus,
		'sends6c': sends6c,
		'sends6bplus': sends6bplus,
		'videosadded': videosadded,
})


def user_list(request):
	users = User.objects.all()
	return render(request, 'users/user_list.html', {
		'users': users,
})

def climb_list(request):
	userlist = User.objects.order_by('id')
	currentuser = request.user
	if request.GET:
		qs = Climb.objects.all()
		qs = qs.annotate(videocount=Count('video', distinct=True)).annotate(starsavg=Avg('userlog__stars', distinct=True)).annotate(gradeavg=Avg('userlog__personal_grade', distinct=True)).annotate(localrepeats=Count('userlog'))
		climbheader = 'Climbs'
		searchname = request.GET.get('name', '')
		searchgrade = request.GET.get('grade', '')
		searchsentby = request.GET.get('sentby', '')
		searchexcludemine = request.GET.get('excludemine', '')
		searchglobalstars = request.GET.get('globalstars', '')
		searchlocalstars = request.GET.get('localstars', '')
		searchsort = request.GET.get('sortby', '')
		if searchname:
			qs = qs.filter(name__icontains=searchname)
		if searchgrade:
			qs = qs.filter(grade=searchgrade)
		if searchsentby:
			qs = qs.filter(userlog__user_id=searchsentby)
		if searchexcludemine == 'true':
			qs = qs.exclude(userlog__user_id=currentuser)
		if searchglobalstars:
			qs = qs.filter(stars=searchglobalstars)
		if searchlocalstars == '3':
			qs = qs.filter(starsavg__gte=3)
		if searchlocalstars == '2':
			qs = qs.filter(starsavg__gte=2)
		if searchlocalstars == '1':
			qs = qs.filter(starsavg__gte=1)
		if searchsort == 'sortgrade':
			qs = qs.order_by('-grade')
		if searchsort == 'sortname':
			qs = qs.order_by('name')
		if searchsort == 'sortlocalrepeats':
			qs = qs.order_by('-localrepeats')
		if searchsort == 'sortlocalstars':
			qs = qs.order_by('-starsavg')
		if searchsort == 'sortvideos':
			qs = qs.order_by('-videocount')
	else:
		qs = Climb.objects.none()
		climbheader = ''
		
	return render(request, 'climbs/climb_list.html', {
		'climb': qs,
		'userlist': userlist,
		'climbheader': climbheader,
})


def edit_profile(request):
    user_profile = request.user.profile()
    url = user_profile.url
