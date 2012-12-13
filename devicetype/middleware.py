import logging
import time

from django.conf import settings
from django.utils.http import cookie_date

from devicetype import conf
from devicetype.browser import check_browser


class DeviceTypeMiddleware(object):
    """
    """

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def process_request(self, request):

        # force switch link
        if 'devicetype' in request.GET and request.GET['devicetype'] in conf.DEVICE_TYPES:
            request.devicetype = request.GET['devicetype']
            return None

        # test saved cookie
        cookie = request.COOKIES.get('devicetype', None)

        if cookie in conf.DEVICE_TYPES:
            request.devicetype = cookie
            return None

        # test for mobile browser
        if not 'HTTP_USER_AGENT' in request.META:
            return None

        request.devicetype = check_browser(request.META['HTTP_USER_AGENT'])
        request.is_mobile = request.devicetype != 'desktop'

        return None

    def process_template_response(self, request, response):
        """
        Modify template path(s) to render based on device mode and returns response
        """

        orig_template_name = response.template_name
        new_template_name = []

        if request.devicetype in conf.DEVICE_TYPES and conf.TEMPLATE_PREFIX[request.devicetype]:
            if isinstance(orig_template_name, (list, tuple)):
                orig_template_name = list(orig_template_name)

            for t in orig_template_name:
                base_name = t.split('/')[-1]
                new_template_name.append(t.replace(base_name, '%s%s' % (conf.TEMPLATE_PREFIX[request.devicetype], base_name)))

            new_template_name.extend(orig_template_name)
            response.template_name = new_template_name

        # set cookie to identify the browser as mobile
        expires_time = time.time() + conf.DEVICE_TYPE_COOKIE_MAXAGE
        expires = cookie_date(expires_time)
        response.set_cookie('devicetype', request.devicetype, domain=settings.SESSION_COOKIE_DOMAIN,
                            max_age=conf.DEVICE_TYPE_COOKIE_MAXAGE, expires=expires)

        return response

#    def process_response(self, request, response):
#
#        # set cookie to identify the browser as mobile
#        expires_time = time.time() + DEFAULT_COOKIE_MAX_AGE
#        expires = cookie_date(expires_time)
#        response.set_cookie('devicetype', request.devicetype, domain=settings.SESSION_COOKIE_DOMAIN,
#            max_age=DEFAULT_COOKIE_MAX_AGE, expires=expires)
#
#        # remove force get parameter
#        if 'devicetype' in request.GET:
#            return HttpResponseRedirect(request.META['PATH_INFO'])
#
#        return response


class RedirectMiddleware:
    # TODO: mobile version(s) on other place...
    pass
