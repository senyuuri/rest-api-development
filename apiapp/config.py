from django.utils.deprecation import MiddlewareMixin

class DisableCSRF(MiddlewareMixin, object):
    """Disable default CSRF protection

    To enable CSRF:
    Remove apiapp.config.DisableCSRF from MIDDILEWARE in settings.py
    """
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)