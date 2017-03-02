from django.shortcuts import render, redirect, reverse
from collection.models import Climb, Video, UserLog, UserDetails
from django.db.models import Count, Avg, Sum, Q, F, IntegerField, Case, Value, When
from collection.forms import NewClimb, LogClimb, AddVideo, EditClimb, EditUserDetails, EditSend
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django import forms


@login_required	
def home(request):
	recent_sends = UserLog.objects.order_by('-date')
	recent_videos = Video.objects.order_by('-date')
	recent_rec = UserLog.objects.filter(recommended='True').order_by('-date')
	return render(request, 'index.html', {
		'recent_sends': recent_sends,
		'recent_videos': recent_videos,
		'recent_rec': recent_rec,
		
})

@login_required	
def climb_detail(request, slug):
	currentuser = request.user
	climb = Climb.objects.get(slug=slug)
	video = Video.objects.filter(climb__slug=slug)
	videocount = Video.objects.filter(climb__slug=slug).count()
	log = UserLog.objects.filter(climb__slug=slug)
	localstars = UserLog.objects.filter(climb__slug=slug).aggregate(Avg('stars'))
	localgrade = UserLog.objects.filter(climb__slug=slug).aggregate(Avg('personal_grade'))
	localsends = UserLog.objects.filter(climb__slug=slug).count()
	if request.GET:
		return render(request, 'log_climb.html', {
			'climbid': climbid,
		})		
	return render(request, 'climbs/climb_detail.html', {
		'localstars': localstars,
		'localsends': localsends,
		'localgrade': localgrade,
        'climb': climb,
		'video': video,
		'log': log,
		'videocount': videocount,
		'currentuser': currentuser,
})

@login_required	
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
		if request.GET:
			climbid = request.GET.get('climbid', '')
			form = LogClimb({'climb':climbid})
		else:
			form = LogClimb()
	
	return render(request, 'log_climb.html', {'form': form})

@login_required	
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
	


	
@login_required		
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
		climbid = request.GET.get('climbid', '')
		form = AddVideo({'climb':climbid})
	return render(request, 'add_video.html', {'form': form})
	
@login_required	
def user_profile(request, uid):
	profile = User.objects.get(id=uid)
	currentuser = request.user
	log = UserLog.objects.filter(user__id=uid).order_by('-personal_grade', '-date')
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
	sends7bplus = UserLog.objects.filter(user__id=uid, personal_grade=8).count()
	sends7b = UserLog.objects.filter(user__id=uid, personal_grade=7).count()
	sends7aplus = UserLog.objects.filter(user__id=uid, personal_grade=6).count()
	sends7a = UserLog.objects.filter(user__id=uid, personal_grade=5).count()
	sends6cplus = UserLog.objects.filter(user__id=uid, personal_grade=4).count()
	sends6c = UserLog.objects.filter(user__id=uid, personal_grade=3).count()
	sends6bplus = UserLog.objects.filter(user__id=uid, personal_grade=2).count()
	videosadded = Video.objects.filter(uploaded_by__id=uid).count()
	if request.GET:
		searchsort = request.GET.get('sortby', '')
		if searchsort == 'sortgrade':
			log = log.order_by('-personal_grade')
		if searchsort == 'sortname':
			log = log.order_by('climb')
		if searchsort == 'sortdate':
			log = log.order_by('-date')
			
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
		'currentuser': currentuser,
})

@login_required	
def user_list(request):
	if request.GET:
		qs = User.objects.all().order_by('userdetails__first_name')
		qs = qs.annotate(sendcount=Count('userlog', distinct=True)).annotate(videocount=Count('video', distinct=True))
		searchname = request.GET.get('name', '')
		searchsort = request.GET.get('sortby', '')
		if searchname:
			qs = qs.filter(userdetails__first_name__icontains=searchname)
		if searchsort == 'sortname':
			qs = qs.order_by('first_name')
		if searchsort == 'sortsends':
			qs = qs.order_by('-sendcount')
		if searchsort == 'sortvideos':
			qs = qs.order_by('-videocount')
	else:
		qs = User.objects.all().order_by('userdetails__first_name')
		qs = qs.annotate(sendcount=Count('userlog', distinct=True)).annotate(videocount=Count('video', distinct=True))
		
		
		
	return render(request, 'users/user_list.html', {
		'qs': qs,
})

@login_required	
def climb_list(request):
	userlist = User.objects.order_by('id')
	currentuser = request.user
	videocount = Video.objects.all().count()
	if request.GET:
		qs = Climb.objects.all().prefetch_related('users')
		climbcount = qs.count()
		qs = qs.annotate(videocount=Count('video', distinct=True)).annotate(starsavg=Avg('userlog__stars', distinct=True)).annotate(gradeavg=Avg('userlog__personal_grade', distinct=True)).annotate(localrepeats=Count('userlog'))
		climbheader = 'Climbs'
		searchname = request.GET.get('name', '')
		searchgrade = request.GET.get('grade', '')
		searchsentby = request.GET.get('sentby', '')
		searchrecommended = request.GET.get('recby', '')
		searchexcludemine = request.GET.get('excludemine', '')
		searchvideosonly = request.GET.get('videosonly', '')
		searchglobalstars = request.GET.get('globalstars', '')
		searchlocalstars = request.GET.get('localstars', '')
		searchsort = request.GET.get('sortby', '')
		if searchname:
			qs = qs.filter(name__icontains=searchname)
		if searchgrade:
			qs = qs.filter(grade=searchgrade)
		if searchsentby:
			qs = qs.filter(userlog__user_id=searchsentby)
		if searchrecommended:
			qs = qs.filter(Q(userlog__user_id=searchrecommended) & Q(userlog__recommended='True'))
		if searchexcludemine == 'true':
			qs = qs.exclude(userlog__user_id=currentuser)
		if searchvideosonly == 'true':
			qs = qs.exclude(videocount=0)
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
		if searchsort == 'sortglobalrepeats':
			qs = qs.order_by('-global_repeats')
		if searchsort == 'sortname':
			qs = qs.order_by('name')
		if searchsort == 'sortlocalrepeats':
			qs = qs.order_by('-localrepeats')
		if searchsort == 'sortlocalstars':
			qs = qs.order_by('-starsavg')
		if searchsort == 'sortvideos':
			qs = qs.order_by('-videocount')
		
	else:
		qs = Climb.objects.none().prefetch_related('users')
		climbcount = Climb.objects.all().count()
		climbheader = ''
		users = UserLog.objects.none()
		
	return render(request, 'climbs/climb_list.html', {
		'climb': qs,
		'userlist': userlist,
		'climbheader': climbheader,
		'climbcount': climbcount,
		'videocount': videocount,
})


@login_required
def edit_climb(request,slug):
	climb = Climb.objects.get(slug=slug)
	climbs_count = Climb.objects.count()
	form_class = EditClimb
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=climb)
		if form.is_valid():
			form.save()
			return redirect('climb_detail', slug=climb.slug)
	else:
		form = form_class(instance=climb)
	return render(request, 'climbs/edit_climb.html', {
		'climb': climb,
		'form': form,
		
		
})

@login_required	
def send_detail(request, sendid):
	send = UserLog.objects.get(id=sendid)
	return render(request, 'sends/send_detail.html', {
		'send': send,
})

@login_required	
def edit_send(request, sendid):
	currentuser = request.user
	send = UserLog.objects.get(id=sendid)
	if send.user.id == currentuser.id or currentuser.id == 1:
		form_class = EditSend
		if request.method == 'POST':
			form = form_class(data=request.POST, instance=send)
			if form.is_valid():
				form.save()
				return redirect('climb_detail', slug=send.climb.slug)
		else:
			form = form_class(instance=send)
		return render(request, 'sends/edit_send.html', {
			'form': form,
			'send': send,
			
		})
	else:
		return render(request, 'index.html')
		
@login_required
def stats(request):
	this_month = datetime.now().month
	qs = User.objects.all()
	monthsends = qs.annotate(sends=Sum(Case(When(userlog__date__month=this_month, then=1), default=0, output_field=IntegerField()))).order_by('-sends')[:3]
	totalsends = qs.annotate(sends = Count('userlog')).order_by('-sends')[:3]
	monthpoints = qs.annotate(sixbpluspoints=Sum(Case(When(userlog__personal_grade=2, userlog__date__month=this_month, then=1), default=0, output_field=IntegerField()))).annotate(sixcpoints=Sum(Case(When(userlog__personal_grade=3, userlog__date__month=this_month,  then=2), default=0, output_field=IntegerField()))).annotate(sixcpluspoints=Sum(Case(When(userlog__personal_grade=4, userlog__date__month=this_month,  then=4), default=0, output_field=IntegerField()))).annotate(sevenapoints=Sum(Case(When(userlog__personal_grade=5, userlog__date__month=this_month,  then=8), default=0, output_field=IntegerField()))).annotate(sevenapluspoints=Sum(Case(When(userlog__personal_grade=6, userlog__date__month=this_month,  then=16), default=0, output_field=IntegerField()))).annotate(sevenbpoints=Sum(Case(When(userlog__personal_grade=7, userlog__date__month=this_month,  then=32), default=0, output_field=IntegerField()))).annotate(sevenbpluspoints=Sum(Case(When(userlog__personal_grade=8, userlog__date__month=this_month,  then=64), default=0, output_field=IntegerField()))).annotate(sevencpoints=Sum(Case(When(userlog__personal_grade=9, userlog__date__month=this_month,  then=128), default=0, output_field=IntegerField()))).annotate(sevencpluspoints=Sum(Case(When(userlog__personal_grade=10, userlog__date__month=this_month,  then=256), default=0, output_field=IntegerField()))).annotate(eightapoints=Sum(Case(When(userlog__personal_grade=11, userlog__date__month=this_month,  then=512), default=0, output_field=IntegerField()))).annotate(eightapluspoints=Sum(Case(When(userlog__personal_grade=12, userlog__date__month=this_month,  then=1028), default=0, output_field=IntegerField()))).annotate(eightbpoints=Sum(Case(When(userlog__personal_grade=13, userlog__date__month=this_month,  then=2056), default=0, output_field=IntegerField()))).annotate(totalpoints = F('sixbpluspoints') + F('sixcpoints') + F('sixcpluspoints') + F('sevenapoints') + F('sevenapluspoints') + F('sevenbpoints') + F('sevenbpluspoints') + F('sevencpoints') + F('sevencpluspoints') + F('eightapoints') + F('eightapluspoints') + F('eightbpoints')).order_by('-totalpoints')[:3]
	
	totalpoints = qs.annotate(sixbpluspoints=Sum(Case(When(userlog__personal_grade=2, then=1), default=0, output_field=IntegerField()))).annotate(sixcpoints=Sum(Case(When(userlog__personal_grade=3, then=2), default=0, output_field=IntegerField()))).annotate(sixcpluspoints=Sum(Case(When(userlog__personal_grade=4, then=4), default=0, output_field=IntegerField()))).annotate(sevenapoints=Sum(Case(When(userlog__personal_grade=5, then=8), default=0, output_field=IntegerField()))).annotate(sevenapluspoints=Sum(Case(When(userlog__personal_grade=6, then=16), default=0, output_field=IntegerField()))).annotate(sevenbpoints=Sum(Case(When(userlog__personal_grade=7, then=32), default=0, output_field=IntegerField()))).annotate(sevenbpluspoints=Sum(Case(When(userlog__personal_grade=8, then=64), default=0, output_field=IntegerField()))).annotate(sevencpoints=Sum(Case(When(userlog__personal_grade=9, then=128), default=0, output_field=IntegerField()))).annotate(sevencpluspoints=Sum(Case(When(userlog__personal_grade=10, then=256), default=0, output_field=IntegerField()))).annotate(eightapoints=Sum(Case(When(userlog__personal_grade=11, then=512), default=0, output_field=IntegerField()))).annotate(eightapluspoints=Sum(Case(When(userlog__personal_grade=12, then=1028), default=0, output_field=IntegerField()))).annotate(eightbpoints=Sum(Case(When(userlog__personal_grade=13, then=2056), default=0, output_field=IntegerField()))).annotate(totalpoints = F('sixbpluspoints') + F('sixcpoints') + F('sixcpluspoints') + F('sevenapoints') + F('sevenapluspoints') + F('sevenbpoints') + F('sevenbpluspoints') + F('sevencpoints') + F('sevencpluspoints') + F('eightapoints') + F('eightapluspoints') + F('eightbpoints')).order_by('-totalpoints')[:3]
	
	return render(request, 'stats/stats.html', {
		
		'monthpoints': monthpoints,
		'monthsends': monthsends,
		'totalsends': totalsends,
		'totalpoints': totalpoints,
		
	
		
})
		

@login_required	
def delete_send(request, sendid):
	currentuser = request.user
	send = UserLog.objects.get(id=sendid)
	if send.user.id == currentuser.id or currentuser.id == 1:
		return render(request, 'sends/delete_send.html', {
			'send': send,
		})
	else:
		return render(request, 'index.html')
		
		
@login_required	
def delete_confirm(request, sendid):
	currentuser = request.user
	send = UserLog.objects.get(id=sendid).delete()
	
	return redirect('user_profile', uid=currentuser.id)
	


@login_required
def user_details(request):
	currentuser = request.user
	return render(request, 'user_details.html', {
		'currentuser': currentuser,
})

@login_required
def edit_details(request):
	user = request.user.userdetails
	form_class = EditUserDetails
	if request.method == 'POST':
		form = form_class(data=request.POST, instance=user)
		if form.is_valid():
			form.save()
			return redirect('user_details')
	else:
		form = form_class(instance=user)
	return render(request, "edit_user_details.html", {
		'form': form,
		'user': user,
})


	
def logout_view(request):
	logout(request)
	return render(request, 'registration/logout.html')

	
def weather_chart_view(request):
    #Step 1: Create a DataPool with the data we want to retrieve.
    weatherdata = \
        DataPool(
           series=
            [{'options': {
               'source': MonthlyWeatherByCity.objects.all()},
              'terms': [
                'month',
                'houston_temp',
                'boston_temp']}
             ])

    #Step 2: Create the Chart object
    cht = Chart(
            datasource = weatherdata,
            series_options =
              [{'options':{
                  'type': 'line',
                  'stacking': False},
                'terms':{
                  'month': [
                    'boston_temp',
                    'houston_temp']
                  }}],
            chart_options =
              {'title': {
                   'text': 'Weather Data of Boston and Houston'},
               'xAxis': {
                    'title': {
                       'text': 'Month number'}}})

    #Step 3: Send the chart object to the template.
    return render_to_response({'weatherchart': cht})

