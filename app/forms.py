from django import newforms as forms
from mittens.modules.models import Module

class ModuleInstanceForm(forms.Form):
    module_path = forms.ChoiceField()
    
    def __init__(self, installed_modules, *args, **kwargs):
        super(ModuleInstanceForm, self).__init__(*args, **kwargs)
        self.fields['module_path'].choices = installed_modules.get_path_choices()
        
    def get_add_url(self, data):
        module = Module.from_path(data['module_path'])
        return module.admin_add_root