from django.template import RequestContext
from django.shortcuts import render_to_response
from mittens.app.models import Site

def index(request):
    return render_to_response('index.html', {
        'sites': Site.objects.all(),
    }, context_instance=RequestContext(request))
