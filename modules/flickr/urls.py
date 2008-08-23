from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$',                'mittens.modules.flickr.views.module'),
    (r'^module/$',         'mittens.modules.flickr.views.module2'),
    (r'^module/more/$',    'mittens.modules.flickr.views.module3'),
    (r'^admin/add/$',      'mittens.modules.flickr.views.adminadd'),	# e.g. /admin/add/flickr/
    (r'^admin/edit/$',     'mittens.modules.flickr.views.admin'),	# e.g. /admin/edit/my-flickr/
    (r'^admin/edit/sub/$', 'mittens.modules.flickr.views.admin2'),	# e.g. /admin/edit/my-flickr/sub/
)