from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^all/$', 'mysite.article.views.articles'),
    url(r'^get/(?P<article_id>\d+)/$', 'mysite.article.views.article'),
    url(r'^create/$', 'mysite.article.views.create'),
)

