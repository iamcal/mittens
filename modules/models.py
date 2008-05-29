from django.template import loader
from django.core.urlresolvers import get_resolver
from mittens import settings

class Module:

    link = None		# points to the ModuleLink for this module instance
    request_path = '/'	# the request sub-path

    def _get_module_root(self):
        # in the future, this will be the module 'label' instead
        return "/%s/" % self.link.id
    module_root = property(_get_module_root)

    def _get_admin_root(self):
        return "/%s/%s/" %(settings.APP_ADMIN_PATH, self.link.id)
    admin_root = property(_get_admin_root)

    def _get_module_name(self):
        return self.__class__.__name__.lower()
    module_name = property(_get_module_name)

    def render(self):
        return self.render_template('/')

    def render_module(self):
        return self.render_template('/module' + self.request_path)

    def render_admin(self):
        return self.render_template('/admin' + self.request_path)

    def render_template(self, path):
        resolver = get_resolver('mittens.modules.%s.urls' % self.module_name)
        callback, callback_args, callback_kwargs = resolver.resolve(path)

        settings.request.model = self
        response = callback(settings.request, *callback_args, **callback_kwargs)

        return response