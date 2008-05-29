from django.conf.urls.defaults import *
from mittens import urls
from mittens import settings

urlpatterns = patterns('',
    (r'^$', 'mittens.app.views.mittens'),
    (r'^((?P<moduleid>\d+)/(?P<extra>.*/)?)?$', 'mittens.app.views.extras'),
    (r'^%s/((?P<moduleid>\d+)/(?P<extra>.*/)?)?$' % settings.APP_ADMIN_PATH, 'mittens.app.views.admin'),
)
urlpatterns += urls.urlpatterns