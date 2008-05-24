from django.conf.urls.defaults import *
from mittens import urls
from mittens import settings

urlpattenrs = urls.urlpatterns
urlpatterns += patterns('',
    (settings.INDEX_ADMIN_PATH, include('django.contrib.admin.urls')),
    (r'^$', 'mittens.index.views.index'),
)
