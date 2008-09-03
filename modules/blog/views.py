from django import http
from django.template import RequestContext
from django.template import loader
from mittens.modules.blog.models import BlogForm

def module(request):
    return loader.render_to_string('blog.html', {
        'blog': request.model,
    }, context_instance=RequestContext(request))

def admin(request):
    return loader.render_to_string('blog/edit.html', {
        'blog': request.model,
    }, context_instance=RequestContext(request))
    
def add(request):

    if request.method == 'POST':
        form = BlogForm(request.site, request.POST)
        if form.is_valid():
            blog = form.save_instance()
            # TODO - return a more useful string
            #return http.HttpResponseRedirect(blog.admin_edit_root)
            return 'Blog created! <a href="%s">Edit your blog?</a>' % blog.admin_edit_root
        else:
            print form.errors
    else:
        form = BlogForm(request.site)

    return loader.render_to_string('blog/add.html', {
        'form': form,
    }, context_instance=RequestContext(request))
