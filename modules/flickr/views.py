from django.template import RequestContext
from django.template import loader

def module(request):
    return loader.render_to_string('flickr.html', {
        'flickr': request.model,
    }, context_instance=RequestContext(request))

def module2(request):
    return loader.render_to_string('flickr2.html', {
        'flickr': request.model,
    }, context_instance=RequestContext(request))

def module3(request):
    return loader.render_to_string('flickr3.html', {
        'flickr': request.model,
    }, context_instance=RequestContext(request))

def admin(request):
    return loader.render_to_string('flickr_admin.html', {
        'flickr': request.model,
    }, context_instance=RequestContext(request))

def admin2(request):
    return loader.render_to_string('flickr_admin2.html', {
        'flickr': request.model,
    }, context_instance=RequestContext(request))

# TODO write real add view
def adminadd(request):
    return loader.render_to_string('flickr_admin2.html', {
    }, context_instance=RequestContext(request))
