from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^simcms/', include('simcms.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    (r'^weblog/$', 'blog.views.entries_index'),
    (r'^weblog/(?P<id>\w+)/$', 'blog.views.entry_detail'),
    (r'^weblog/tag/(?P<id>\w+)/$', 'blog.views.entries_index'),
)

