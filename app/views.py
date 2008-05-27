from django.template import RequestContext
from django.shortcuts import render_to_response

def mittens(request):
    return render_to_response('mittens.html', {
    }, context_instance=RequestContext(request))
    
def admin(request):
    return render_to_response('admin.html', {
    }, context_instance=RequestContext(request))