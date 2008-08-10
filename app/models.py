from django.db import models
from django.core import validators
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from mittens import settings
import datetime

class ModuleInfo:
    def __init__(self, type, settings, path, name):
        self.type = type
        self.settings = settings
        self.path = path
        self.name = name
    
    def add_url(self):
        #return reverse('admin_add', urlconf='app.urls', args=[self.type], kwargs=None)
        #url = reverse('admin_add', urlconf='app.urls', kwargs={'module_type': self.type})
        #print url
        return '/%s/add/%s/' % (settings.APP_ADMIN_PATH, self.type)
        
    @staticmethod
    def from_path(path):
        type = path.rsplit('.', 1)[1].lower()
        # TODO define these in the module settings
        try:
            settings = __import__('%s.settings' % path, '', '', 'settings')
            name = settings.DISPLAY_NAME
        except:
            settings = None
            name = type.capitalize()
        return ModuleInfo(type, settings, path, name)

class InstalledModules:

    def __init__(self):
        # create a module definition for each installed module
        self.modules = []
        for path in settings.INSTALLED_MODULES:
            self.modules.append(ModuleInfo.from_path(path))

    def get_path_choices(self):
        choices = []
        for module in self.modules:
            choices.append((module.path, module.name))
        return choices


class Site(models.Model):
    subdomain = models.CharField(_('subdomain'), max_length=63, unique=True, db_index=True, validator_list=[validators.isAlphaNumeric])
    name = models.CharField(_('name'), max_length=255) # display name (e.g. Leah's Mittens)
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)
    #template = models.CharField(_('template'), max_length=255) # template name (e.g. '3-column')

    def __unicode__(self):
        return self.name

    class Admin:
        list_display = ('subdomain', 'name')

class ModuleLink(models.Model):
    site = models.ForeignKey(Site, primary_key=False, related_name='modules', raw_id_admin=True)
    module_type = models.CharField(_('module type name'), max_length=255) # e.g. blog
    module_id = models.PositiveIntegerField(_('module id'))
    module_label = models.SlugField(_('slug field'), db_index=True)
    in_column = models.PositiveIntegerField(_('in column'), default=0)
    in_order = models.PositiveIntegerField(_('in order'), default=0)

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
        instance = model.objects.get(id=self.module_id)
        instance.link = self
        return instance
    module = property(_get_module)

