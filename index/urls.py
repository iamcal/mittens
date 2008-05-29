from django.conf.urls.defaults import *
from mittens import urls
from mittens import settings

urlpatterns = patterns('',
    (r'^%s/' % settings.INDEX_ADMIN_PATH, include('django.contrib.admin.urls')),
    (r'^$', 'mittens.index.views.index'),
)
urlpatterns += urls.urlpatterns