from django.db import models
from django.utils.translation import ugettext_lazy as _
from mittens.modules.models import Module
import datetime

class Flickr(Module, models.Model):
    # site
    name = models.CharField(_('name'), max_length=255)
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.name
        
    class Admin:
        list_display = ('id', 'name', 'date_created')
