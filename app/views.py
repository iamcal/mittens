from django.template import RequestContext
from django.shortcuts import render_to_response
from mittens.app import models

def mittens(request):
    return render_to_response('mittens.html', {
    }, context_instance=RequestContext(request))
    
def admin(request, moduleid=0, extra=''):

    module = None

    try:
        module = models.ModuleLink.objects.get(id=moduleid).module
    except:
        print "no object thingy - try and get the default module, then redirect"

    # this is inside try/except because {module} might be None
    # and extra might be None. still seems to always do the right
    # thing, but it's U.G.L.Y.
    try:
        module.admin_request_path = '/' + extra
    except:
        pass


    return render_to_response('admin.html', {
        'current_module': module,
    }, context_instance=RequestContext(request))