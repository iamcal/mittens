from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$',       'mittens.modules.blog.views.module'),
    (r'^admin/$', 'mittens.modules.blog.views.admin'),
)