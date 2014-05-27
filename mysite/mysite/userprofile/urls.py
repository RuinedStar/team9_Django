from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'mysite.userprofile.views.user_profile'),
)