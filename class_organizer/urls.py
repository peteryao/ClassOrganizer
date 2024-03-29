from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'class_organizer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('core.urls')),
    url(r'^admin/', include(admin.site.urls)),
) 

urlpatterns += staticfiles_urlpatterns()