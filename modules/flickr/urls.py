from django.conf.urls.defaults import *

urlpatterns = patterns('mittens.modules.flickr.views',
    url(r'^$',            'module',   name='module'),
    url(r'^module/$',     'module2',  name='extra'),
    (r'^module/more/$',   'module3'),
    url(r'^admin/add/$',  'adminadd', name='admin_add'),	# e.g. /admin/add/flickr/
    url(r'^admin/edit/$', 'admin',    name='admin_edit'),	# e.g. /admin/edit/my-flickr/
    (r'^admin/edit/sub/$', 'admin2'),	# e.g. /admin/edit/my-flickr/sub/
)