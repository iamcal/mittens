from django import newforms as forms
from mittens.app.models import ModuleInfo

class ModuleLinkForm(forms.Form):
    module_path = forms.ChoiceField()
    
    def __init__(self, installed_modules, *args, **kwargs):
        self.module_info = None
        super(ModuleLinkForm, self).__init__(*args, **kwargs)
        self.fields['module_path'].choices = installed_modules.get_path_choices()
    
    def update(self, data):
        self.module_info = ModuleInfo.from_path(data['module_path'])
        
    def get_add_url(self):
        print 'adf'
        
    def save(self, data):
        print data
        '''
        module_link = ModuleLink(
                site = '',
                module_type = data['module_type'],
                module_id = models.PositiveIntegerField(_('module id'))
                module_label = 'temp',
            )
        '''