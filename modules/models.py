from django.template import loader
from mittens import settings

class Module:

    link = None
    admin_request_path = '/'

    def _get_admin_root(self):
        return "/%s/%s/" %(settings.APP_ADMIN_PATH, self.link.id)
    admin_root = property(_get_admin_root)

    def _get_module_name(self):
        return self.__class__.__name__.lower()
    module_name = property(_get_module_name)
    
    def _get_template_name(self):
        return '%s.html' % self.module_name
    template_name = property(_get_template_name)

    def render(self):
        # render the cubby html
        return loader.render_to_string(self.template_name, {
            self.module_name: self,
        })

    def render_admin(self):
        return "admin module for id %s (instance %s of %s) at path %s" %(self.link.id, self.id, self.link.module_type, self.admin_request_path)
