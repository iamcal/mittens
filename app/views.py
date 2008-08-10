from django.template import RequestContext
from django.shortcuts import render_to_response
from django import http
from mittens.app import models
from mittens.app import forms
from mittens import settings

def mittens(request, edit_mode=False):
    settings.request = request

    return render_to_response('mittens.html', {
        'edit_mode': edit_mode,
    }, context_instance=RequestContext(request))

def extras(request, moduleid=0, extra=''):
    settings.request = request
    module = get_this_module(moduleid, extra)

    return render_to_response('extras.html', {
        'current_module': module,
    }, context_instance=RequestContext(request))
    
def admin_edit(request, moduleid=0, extra=''):
    settings.request = request
    module = get_this_module(moduleid, extra)

    if not module:
        try: # cal - exception handling is FAST in python, heh
            # get the first module
            # TODO make this the first by user pref
            module = request.site.modules.all()[0]
        except IndexError:
            print "oops - we need to show a 'no modules' page..."
        else: # TODO use reverse() function
            url = "/admin/edit/%s/" % module.id
            return http.HttpResponseRedirect(url)
    
    if request.method == 'POST':
        print request.POST
        form = forms.ModuleLinkForm(request.installed_modules, request.POST)
        if form.is_valid():
            form.update(form.cleaned_data)
            add_url = form.get_add_url()
            if add_url:
                return http.HttpResponseRedirect(add_url)
            #form.save(form.cleaned_data)
            #form.save_or_redirect(form.cleaned_data)
        else:
            print form.errors
    else:
        form = forms.ModuleLinkForm(request.installed_modules)

    return render_to_response('admin/edit.html', {
        'admin_mode': 'EDIT',
        'current_module': module,
        'form': form,
    }, context_instance=RequestContext(request))


def get_this_module(moduleid, extra):

    try:
        module = models.ModuleLink.objects.get(id=moduleid).module
    except:
        return None

    # this is inside try/except because extra might be None
    try:
        module.request_path = '/' + extra
    except:
        pass

    return module