from django.conf.urls import patterns, include, url

urlpatterns = patterns('mysite.Cachapon.views',

	url(r'^$', 'Home'),
	url(r'^bag/$','LookYourBag'),
	url(r'^cacha/$','CachaEgg'),
)