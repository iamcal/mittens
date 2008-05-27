from django.template import RequestContext
from django.shortcuts import render_to_response
from mittens.app import models

def mittens(request):
    return render_to_response('mittens.html', {
    }, context_instance=RequestContext(request))
    
def admin(request, moduleid=0, extra=''):

    try:
        link = models.ModuleLink.objects.get(id=moduleid)
        module = link.module
        module.admin_request_path = '/' + extra
    except:
        link = None
        print "no object thingy - try and get the default module, then redirect"

    return render_to_response('admin.html', {
        'current_module': module,
    }, context_instance=RequestContext(request))