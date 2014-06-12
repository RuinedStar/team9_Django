from django.conf.urls import patterns, url
urlpatterns = patterns('mysite.Cachapon.views',

	url(r'^$', 'Home'),
	url(r'^shop/$','Shop'),
	url(r'^cacha/$','CachaEgg'),
	url(r'^box/$','LookYourBox'),
)
