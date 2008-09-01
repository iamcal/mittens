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
    print 'add new blog! need a form'
    print request.method

    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            print 'form is valid'
        else:
            print form.errors
    else:
        form = BlogForm()

    return loader.render_to_string('blog/add.html', {
        'form': form,
    }, context_instance=RequestContext(request))
