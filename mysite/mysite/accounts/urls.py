from django.conf.urls import patterns, include, url

urlpatterns = patterns('mysite.accounts.views',

	url(r'^accounts/login/$', login),
	url(r'^accounts/auth/$', auth_view),
	url(r'^accounts/logout/$', logout),
	url(r'^accounts/loggedin/$', loggedin),
	url(r'^accounts/invalid/$', invalid_login),
)