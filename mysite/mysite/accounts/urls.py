from django.conf.urls import patterns, include, url

urlpatterns = patterns('mysite.accounts.views',

	url(r'^login/$', 'login'),
	url(r'^auth/$', 'auth_view'),
	url(r'^logout/$', 'logout'),
	url(r'^loggedin/$', 'loggedin'),
	url(r'^invalid/$', 'invalid_login'),
)