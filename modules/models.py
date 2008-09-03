from django.template import loader
from django.core.urlresolvers import get_resolver, Resolver404, NoReverseMatch
from django.core import validators
import django.newforms as forms
from mittens.app.models import ModuleInstance
from mittens import settings

# base class for each type of module
class Module:

    instance = None		# points to the ModuleInstance
    request_path = ''	# the request sub-path

    @staticmethod
    def from_path(path):
        type = path.rsplit('.', 1)[1].lower()
        return Module.from_type(type)
    
    @staticmethod
    def from_type(type):
        module = Module()
        module.type = type
        return module
    
    def _get_type(self):
        return self.__class__.__name__.lower()
    type = property(_get_type)
    
    def _get_path(self):
        return 'mittens.modules.%s' % self.type
    path = property(_get_path)
    
    def _get_url_path(self):
        return '%s.urls' % self.path
    url_path = property(_get_url_path)

    def _get_settings(self):
        # throws ImportError if settings file is missing
        return __import__('%s.settings' % self.path, '', '', 'settings')
    settings = property(_get_settings)
    
    def _get_display_name(self):
        try:
            return self.settings.DISPLAY_NAME
        except ImportError:
            return self.type.capitalize()
    display_name = property(_get_display_name)

    def _get_module_root(self):
        return "/%s/" % self.instance.module_label
    module_root = property(_get_module_root)

    def _get_admin_edit_root(self):
        return "/%s/edit/%s/" %(settings.APP_ADMIN_PATH, self.instance.module_label)
    admin_edit_root = property(_get_admin_edit_root)

    def _get_admin_add_root(self):
        return "/%s/add/%s/" %(settings.APP_ADMIN_PATH, self.type)
    admin_add_root = property(_get_admin_add_root)
    
    def _path_from_name(self, resolver, name):
        return '/%s%s' % (resolver.reverse(name), self.request_path)
    
    def render_template(self, request, name):
        
        resolver = get_resolver(self.url_path)
        try:
            path = self._path_from_name(resolver, name)
        except NoReverseMatch:
            return 'Error: cannot find url named "%s" in %s' % (name, self.url_path)

        print 'debug:', name, path

        try:
            callback, callback_args, callback_kwargs = resolver.resolve(path)
        except Resolver404:
            return 'Error: missing url resolver for path %s in %s' % (path, self.url_path)

        request.model = self
        response = callback(request, *callback_args, **callback_kwargs)

        return response

class ModuleForm(forms.ModelForm):

    label = forms.RegexField(regex=validators.slug_re)
    
    def __init__(self, site, *args, **kwargs):
        self.site = site
        super(ModuleForm, self).__init__(*args, **kwargs)
    
    def clean_label(self):
        label = self.cleaned_data['label']
        try: # check for dupe labels in my site
            ModuleInstance.objects.get(site=self.site, module_label=label)
            raise forms.ValidationError('Label must be unique to your site.')
        except ModuleInstance.DoesNotExist:
            pass
        return label

    def save_instance(self):
        module = self.save()
        # tie the module to a ModuleInstance object for this site
        instance = ModuleInstance(
                site=self.site,
                module_type=module.type,
                module_id=module.id,
                module_label=self.cleaned_data['label'],
            )
        instance.save()
        module.instance = instance
        return module
        
    class Meta:
        fields = ('label') # required for each module form