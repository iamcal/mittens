from django.conf.urls.defaults import *

urlpatterns = patterns('mittens.modules.blog.views',
    url(r'^$',            'module', name='module'),
    url(r'^admin/add/$',  'add',    name='admin_add'),  # e.g. /admin/add/blog/
    url(r'^admin/edit/$', 'admin',  name='admin_edit'), # e.g. /admin/edit/my-blog/
)