from django.template import RequestContext
from django.template import loader

def module(request):
    return loader.render_to_string('blog.html', {
        'blog': request.model,
    }, context_instance=RequestContext(request))

def admin(request):
    return loader.render_to_string('blog_admin.html', {
        'blog': request.model,
        'r': request,
    }, context_instance=RequestContext(request))
