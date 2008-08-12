from django.conf.urls.defaults import *
from mittens import urls
from mittens import settings

urlpatterns = patterns('mittens.app.views',
    (r'^$', 'mittens'),
    #(r'^edit/$', 'mittens.app.views.mittens', {'edit_mode': True}),
    (r'^((?P<moduleid>\d+)/(?P<extra>.*/)?)?$', 'extras'),
    #(r'^%s/((?P<moduleid>\d+)/(?P<extra>.*/)?)?$' % settings.APP_ADMIN_PATH, 'mittens.app.views.admin'),
    
    (r'^%s/edit/((?P<module_label>[\w-]+)/(?P<extra>.*/)?)?$' % settings.APP_ADMIN_PATH, 'admin_edit'),
    #(r'^%s/layout/$' % settings.APP_ADMIN_PATH, 'mittens', {'edit_mode': True}),
    (r'^%s/layout/$' % settings.APP_ADMIN_PATH, 'admin_layout'),
    (r'^%s/add/(?P<module_type>[\w-]+)/$' % settings.APP_ADMIN_PATH, 'admin_add'),
)
urlpatterns += urls.urlpatterns