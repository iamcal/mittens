from django.template import loader
from django.core.urlresolvers import get_resolver, Resolver404
from mittens import settings

# base class for each type of module
class Module:

    instance = None		# points to the ModuleInstance
    request_path = '/'	# the request sub-path
    settings = None
    display_name = None

    @staticmethod
    def from_path(path):
        type = path.rsplit('.', 1)[1].lower()
        return Module.from_type(type, path)
    
    @staticmethod
    def from_type(type, path=None):
        module = Module()
        module.type = type
        if path is None:
            path = 'mittens.modules.%s' % type
        module.path = path
        # TODO define these in the module settings
        try:
            module.settings = __import__('%s.settings' % path, '', '', 'settings')
            module.display_name = settings.DISPLAY_NAME
        except:
            module.display_name = type.capitalize()
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

    def _get_module_root(self):
        return "/%s/" % self.instance.module_label
    module_root = property(_get_module_root)

    def _get_admin_edit_root(self):
        return "/%s/edit/%s/" %(settings.APP_ADMIN_PATH, self.instance.module_label)
    admin_edit_root = property(_get_admin_edit_root)

    def _get_admin_add_root(self):
        return "/%s/add/%s/" %(settings.APP_ADMIN_PATH, self.type)
    admin_add_root = property(_get_admin_add_root)

    def render(self):
        return self.render_template('/')

    def render_module(self):
        return self.render_template('/module%s' % self.request_path)

    def render_admin_edit(self):
        return self.render_template('/admin/edit%s' % self.request_path)

    def render_admin_add(self):
        return self.render_template('/admin/add%s' % self.request_path)

    def render_template(self, path):
        resolver = get_resolver(self.url_path)
        try:
            callback, callback_args, callback_kwargs = resolver.resolve(path)
        except Resolver404:
            return 'Error: missing url resolver for path %s in %s' % (path, self.url_path)

        settings.request.model = self
        response = callback(settings.request, *callback_args, **callback_kwargs)

        return response