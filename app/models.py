from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
import datetime

class Site(models.Model):
    subdomain = models.CharField(_('subdomain'), max_length=63, unique=True, db_index=True, validator_list=[validators.isAlphaNumeric])
    name = models.CharField(_('name'), max_length=255) # display name (e.g. Leah's Mittens)
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)

    def __unicode__(self):
        return self.name

    class Admin:
        list_display = ('subdomain', 'name')

class ModuleLink(models.Model):
    site = models.ForeignKey(Site, primary_key=False, related_name='modules', raw_id_admin=True)
    module_type = models.CharField(_('module type name'), max_length=255) # e.g. blog
    module_id = models.PositiveIntegerField(_('module id'))
    in_column = models.PositiveIntegerField(_('in column'))
    in_order = models.PositiveIntegerField(_('in order'))

    class Meta:
        ordering = ('in_column', 'in_order',)


    class Admin:
        list_display = ('id', 'site', 'module_type', 'module_id', 'module', 'in_column', 'in_order',)

    def __unicode__(self):
        # returns something like "blog:1 - Cal's lovely blog"
        return '%s:%s - %s' %(self.module_type, self.module_id, self.module.__unicode__())

    # module instance for this link
    def _get_module(self):
        # import the model (e.g. from modules.blog.models import Blog)
        module_name = self.module_type.lower()
        model = getattr(__import__('modules.%s.models' % module_name, '', '', module_name), module_name.capitalize())
        # return instance of module model (e.g. a Blog)
        return model.objects.get(id=self.module_id)
    module = property(_get_module)

