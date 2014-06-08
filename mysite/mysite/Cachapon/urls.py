from django.conf.urls import patterns, include, url

urlpatterns = patterns('mysite.Cachapon.views',

	url(r'^$', 'ImageTest'),
	url(r'^bag/$','LookYourBag'),
)