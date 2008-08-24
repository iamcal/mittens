from django.template import RequestContext
from django.shortcuts import render_to_response
from django import http
from mittens.app import models, forms
from mittens.modules.models import Module
from mittens import settings

def mittens(request):
    settings.request = request
    return render_to_response('mittens.html', {
        'edit_mode': False,
    }, context_instance=RequestContext(request))

def extras(request, module_label, extra=''):
    settings.request = request
    module = get_this_module(module_label, extra)

    return render_to_response('extras.html', {
        'current_module': module,
    }, context_instance=RequestContext(request))
    
def admin_edit(request, module_label, extra=''):
    settings.request = request
    module = get_this_module(module_label, extra)

    if not module:
        try: # cal - exception handling is FAST in python, heh
            # get the first module
            # TODO make this the first by user pref
            module = request.site.modules.all()[0]
        except IndexError:
            print "oops - we need to show a 'no modules' page..."
        else: # TODO use reverse() function
            url = "/admin/edit/%s/" % module.module_label
            return http.HttpResponseRedirect(url)
    
    if request.method == 'POST':
        form = forms.ModuleInstanceForm(request.POST)
        if form.is_valid():
            return http.HttpResponseRedirect(form.get_add_url(form.cleaned_data))
        else:
            print form.errors
    else:
        form = forms.ModuleInstanceForm()

    return render_to_response('admin/edit.html', {
        'admin_mode': 'EDIT',
        'current_module': module,
        'form': form,
    }, context_instance=RequestContext(request))

def admin_layout(request):
    return render_to_response('admin/layout.html', {
        'admin_mode': 'LAYOUT',
        'edit_mode': True,
    }, context_instance=RequestContext(request))
    
def admin_add(request, module_type):
    print 'admin add type: %s' % module_type
    module = Module.from_type(module_type)
    return render_to_response('admin/add.html', {
        'admin_mode': 'ADD',
        'module': module,
        'module_type': module_type,
    }, context_instance=RequestContext(request))


def get_this_module(module_label, extra):

    try:
        module = models.ModuleInstance.objects.get(module_label=module_label).module
    except:
        return None

    # this is inside try/except because extra might be None
    try:
        module.request_path = '/' + extra
    except:
        pass

    return module