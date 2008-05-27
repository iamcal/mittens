from django.conf.urls.defaults import *
from mittens import urls
from mittens import settings

urlpatterns = patterns('',
    (r'^%s/((?P<moduleid>\d+)/(?P<extra>.*/)?)?$' % settings.APP_ADMIN_PATH, 'mittens.app.views.admin'),
    (r'^$', 'mittens.app.views.mittens'),
)
urlpatterns += urls.urlpatterns