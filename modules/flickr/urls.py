from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$',             'mittens.modules.flickr.views.module'),
    (r'^module/$',      'mittens.modules.flickr.views.module2'),
    (r'^module/more/$', 'mittens.modules.flickr.views.module3'),
    (r'^admin/$',       'mittens.modules.flickr.views.admin'),
    (r'^admin/sub/$',   'mittens.modules.flickr.views.admin2'),
)