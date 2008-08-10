from django import newforms as forms
from mittens.app.models import ModuleInfo

class ModuleLinkForm(forms.Form):
    module_path = forms.ChoiceField()
    
    def __init__(self, installed_modules, *args, **kwargs):
        super(ModuleLinkForm, self).__init__(*args, **kwargs)
        self.fields['module_path'].choices = installed_modules.get_path_choices()

    def get_add_url(self, data):
        module_info = ModuleInfo.from_path(data['module_path'])
        return module_info.add_url()