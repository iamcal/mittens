from django import newforms as forms

class ModuleLinkForm(forms.Form):
    module_path = forms.ChoiceField()
    
    def __init__(self, installed_modules, *args, **kwargs):
        super(ModuleLinkForm, self).__init__(*args, **kwargs)
        self.fields['module_path'].choices = installed_modules.get_path_choices()