from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^articles/', include('mysite.article.urls')),
    url(r'^accounts/', include('mysite.accounts.urls')),
    url(r'^accounts/profile/', include('mysite.userprofile.urls')),
    url(r'^Cachapon/', include('mysite.Cachapon.urls')),
    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    #url(r'^hello/$', 'article.views.hello'),
    #url(r'^hello_template/$', 'article.views.hello_template'),
    #url(r'hello_template_simple/$','article.views.hello_template_simple'),
    #url(r'^hello_class_view/$', HelloTemplate.as_view()),

    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
