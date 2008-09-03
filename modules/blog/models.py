from django.db import models
from django.core import validators
from django.utils.translation import ugettext_lazy as _
from mittens.app.models import ModuleInstance
from mittens.modules.models import Module
import django.newforms as forms
import datetime

class Blog(Module, models.Model):
    # site
    name = models.CharField(_('name'), max_length=255)
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)
    
    def __unicode__(self):
        return self.name
    
    #def render(self):
    #    return "I am the Blog class render method - i am special!"
        
    class Admin:
        list_display = ('id', 'name', 'date_created')

# TODO - move __init__, clean_label, and save_instance methods into a generic
# app.models.ModuleForm that extends forms.ModelForm
class BlogForm(forms.ModelForm):

    label = forms.RegexField(regex=validators.slug_re)
    
    def __init__(self, site, *args, **kwargs):
        self.site = site
        super(self.__class__, self).__init__(*args, **kwargs)
    
    def clean_label(self):
        label = self.cleaned_data['label']
        try: # check for dupe labels in my site
            ModuleInstance.objects.get(site=self.site, module_label=label)
            raise forms.ValidationError('Label must be unique to your site.')
        except ModuleInstance.DoesNotExist:
            pass
        return label

    def save_instance(self):
        module = self.save()
        # tie the module to a ModuleInstance object
        instance = ModuleInstance(
                site=self.site,
                module_type=module.type,
                module_id=module.id,
                module_label=self.cleaned_data['label'],
            )
        instance.save()
        module.instance = instance
        return module
        
    class Meta:
        model = Blog
        fields = ('label', 'name')

class Post(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=True)
    body = models.TextField(_('body'), blank=True)
    blog = models.ForeignKey(Blog, primary_key=False, related_name='posts', raw_id_admin=True)
    #author
    slug = models.SlugField(_('slug'), max_length=255, prepopulate_from=('date_posted', 'title'))
    is_published = models.BooleanField()
    is_deleted = models.BooleanField()
    views = models.PositiveIntegerField(_('views'), default=0)
    date_created = models.DateTimeField(_('date created'), default=datetime.datetime.now)
    date_modified = models.DateTimeField(_('date modified'), default=datetime.datetime.now)
    date_posted = models.DateTimeField(_('date posted'), blank=True, null=True)
    num_revisions = models.PositiveIntegerField(_('number of revisions'), editable=False, default=0)

    class Admin:
        list_display = ('blog', 'title', 'date_created', 'date_posted')