from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import datetime

class Site(models.Model):
    name = models.CharField(_('name'), max_length=255)
    subdomain = models.CharField(_('subdomain'), max_length=63, unique=True, db_index=True, validator_list=[validators.isAlphaNumeric])
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)

    class Admin:
        pass