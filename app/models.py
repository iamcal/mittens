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

class Blog(models.Model):
    name = models.CharField(_('name'), max_length=255)
    # site
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)
        
    class Admin:
        pass

class Post(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    body = models.TextField(_('body'), blank=True)
    #blog
    #author
    slug = models.SlugField(_('slug'), max_length=255, prepopulate_from=('date_posted', 'title'))
    is_published = models.BooleanField()
    is_deleted = models.BooleanField()
    views = models.PositiveIntegerField(_('views'), default=0)
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)
    date_posted = models.DateTimeField(_('date posted'), blank=True)
    num_revisions = models.PositiveIntegerField(_('number of revisions'), editable=False, default=0)

    class Admin:
        pass