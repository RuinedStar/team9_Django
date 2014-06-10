from django.conf.urls import patterns, url
urlpatterns = patterns('mysite.Cachapon.views',

	url(r'^$', 'Home'),
	url(r'^box/$','LookYourBox'),
	url(r'^cacha/$','CachaEgg'),
)
