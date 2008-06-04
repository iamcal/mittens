from django import newforms as forms

class ModuleLinkForm(forms.Form):
    module_type = forms.ChoiceField()
    
    def __init__(self, installed_modules, *args, **kwargs):
        super(ModuleLinkForm, self).__init__(*args, **kwargs)
        self.fields['module_type'].choices = installed_modules.get_choices()
    
    def save(self, data):
        print data
        module_link = ModuleLink(
                site = '',
                module_type = data['module_type'],
                module_id = models.PositiveIntegerField(_('module id'))
                module_label = 'temp',
            )