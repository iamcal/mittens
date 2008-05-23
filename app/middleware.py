from django.http import Http404, HttpResponseRedirect
from mittens import settings
from mittens.app.models import Site
import re

class SubdomainMiddleware:
    def process_request(self, request):
        """
        Sets the site subdomain based on the request url.
        """
        request.site = None
        parts = request.get_host().split(':', 1)
        host = parts[0]
        try:
            port = ':%s' % parts[1]
        except IndexError:
            port = ''
        print host, port
        # remove www
        if host.startswith('www.'):
            return HttpResponseRedirect('http://%s%s' % (host.lstrip('www.'), port))
        main_re = re.compile('^%s$' % settings.INSTALL_DOMAIN, re.IGNORECASE)
        subdomain_re = re.compile('^([a-z0-9]{1,63})\.%s$' % settings.INSTALL_DOMAIN, re.IGNORECASE)
        if main_re.match(host):
            # no site specified
            print 'root site!'
            return None
        match = subdomain_re.match(host)
        if match:
            site_subdomain = match.group(1)
            print site_subdomain
            try:
                request.site = Site.objects.get(subdomain=site_subdomain)
                return None
            except Site.DoesNotExist:
                raise Http404('Blog not found.')
        # TODO match against site_subdomain from db
        print 'site not matched!'
        return None