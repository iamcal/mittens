from django.template import loader

class Module:
    
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