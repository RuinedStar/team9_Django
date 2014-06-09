from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^articles/', include('mysite.article.urls')),
    url(r'^accounts/', include('mysite.accounts.urls')),
    url(r'^Cachapon/', include('mysite.Cachapon.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL,  document_root = settings.MEDIA_ROOT)
