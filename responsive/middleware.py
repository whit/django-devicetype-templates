import time
from django.conf import settings
import logging

from responsive.browser import check_browser

DEFAULT_COOKIE_MAX_AGE = 60 * 60 * 4


class BrowserMiddleware(object):
    """
    """

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def process_request(self, request):
        # test force cookie first
        cookie = request.COOKIES.get('responsive_mode', None)

        if cookie in ('m', 't', 'b'):
            request.responsive_mode = cookie
            return None

        # test for mobile browser
        if not 'HTTP_USER_AGENT' in request.META:
            return None
        request.responsive_mode = check_browser(request.META['HTTP_USER_AGENT'])
        request.is_mobile = True
        return None

    """

            # set cookie to identify the browser as mobile
            max_age = getattr(settings, 'MOBILE_COOKIE_MAX_AGE', DEFAULT_COOKIE_MAX_AGE)
            expireses_time = time.time() + max_age
            expires = cookie_date(expires_time)
            response.set_cookie('ismobile', '1', domain=settings.SESSION_COOKIE_DOMAIN, max_age=max_age, expires=expires)
            return response

    """

    def process_template_response(self, request, response):
        """
        Modify template/s to render based on device mode and returns response
        """

        t = response.template_name

        print "orig templates: %s" % t

        if request.responsive_mode in ('m', 't'):
            if isinstance(t, (list, tuple)):
                t = list(t)

            response.template_name = "%s-%s" % (request.responsive_mode, response.template_name)

        return response


class RedirectMiddleware:
    # TODO: mobile version(s) on other place...
    pass
