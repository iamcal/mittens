from django.conf.urls.defaults import *
from mittens import urls
from mittens import settings

urlpatterns = urls.urlpatterns
urlpatterns += patterns('',
    (settings.APP_ADMIN_PATH, 'mittens.app.views.admin'),
    (r'^$', 'mittens.app.views.mittens'),
)
