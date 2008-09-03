from django.db import models
from django.utils.translation import ugettext_lazy as _
from mittens.modules.models import Module, ModuleForm
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

class BlogForm(ModuleForm):

    class Meta:
        model = Blog
        fields = ('name')

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