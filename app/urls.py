from django.conf.urls.defaults import *
from mittens.app.models import InstalledModules
from mittens import urls
from mittens import settings

urlpatterns = patterns('mittens.app.views',
    (r'^$', 'mittens'),
    #(r'^edit/$', 'mittens.app.views.mittens', {'edit_mode': True}),
    #(r'^((?P<moduleid>\d+)/(?P<extra>.*/)?)?$', 'extras'),
    #(r'^%s/((?P<moduleid>\d+)/(?P<extra>.*/)?)?$' % settings.APP_ADMIN_PATH, 'mittens.app.views.admin'),
    
    (r'^%s/layout/$' % settings.APP_ADMIN_PATH, 'admin_layout'),
    #(r'^%s/((?P<module_label>[\w-]+)/$' % settings.APP_ADMIN_PATH, include('modules.%s.urls' % module_label)),

    (r'^%s/edit/((?P<module_label>[\w-]+)/(?P<extra>.*/)?)?$' % settings.APP_ADMIN_PATH, 'admin_edit'),
    #(r'^%s/layout/$' % settings.APP_ADMIN_PATH, 'mittens', {'edit_mode': True}),
    (r'^%s/add/(?P<module_type>[\w-]+)/$' % settings.APP_ADMIN_PATH, 'admin_add'),
)

# namespace for each module and it's admin
for module in InstalledModules().modules:
    urlpatterns += patterns('%s.views' % module.path,
        (r'^%s/$' % module.type, include('%s.urls' % module.path)), # /flickr/
        # maybe this is the way to do it, maybe not
        #(r'^%s/add/%s/$' % (settings.APP_ADMIN_PATH, module.type), 'admin_add'), # /admin/add/flickr/
        #(r'^%s/edit/%s/$' % (settings.APP_ADMIN_PATH, module.type), 'admin_edit'), # /admin/edit/flickr/
        #(r'^%s/%s/$' % (settings.APP_ADMIN_PATH, module.type), include('%s.urls' % module.path)), # /admin/flickr/
    )

# static content urls
urlpatterns += urls.urlpatterns