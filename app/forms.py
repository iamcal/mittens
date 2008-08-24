from django import newforms as forms
from mittens.app.models import InstalledModules
from mittens.modules.models import Module

class ModuleInstanceForm(forms.Form):
    module_type = forms.ChoiceField(choices=InstalledModules().get_type_choices())
        
    def get_add_url(self, data):
        module = Module.from_type(data['module_type'])
        return module.admin_add_root