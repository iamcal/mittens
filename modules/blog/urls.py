from django.conf.urls.defaults import *

urlpatterns = patterns('mittens.modules.blog.views',
    (r'^$',            'module'),
    (r'^admin/edit/$', 'admin'),
    (r'^admin/add/$',  'add'),
)