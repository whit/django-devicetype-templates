import logging
import time

from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.http import cookie_date

from devicetype import conf
from devicetype.browser import check_browser


class DeviceTypeMiddleware(object):
    """
    """

    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)

    def process_request(self, request):

        # force switch device type, set cookie and return redirect
        if 'devicetype' in request.GET and request.GET['devicetype'] in conf.DEVICE_TYPES:
            response = HttpResponseRedirect(request.META['PATH_INFO'])
            response.set_cookie('devicetype', request.GET['devicetype'], domain=settings.SESSION_COOKIE_DOMAIN,
                                max_age=conf.DEVICE_TYPE_COOKIE_MAXAGE, expires=self._get_expires())

            return response

        # set type from saved cookie and return
        cookie = request.COOKIES.get('devicetype', None)
        if cookie in conf.DEVICE_TYPES:
            request.devicetype = cookie
            return None

        # check type by UA string, if present
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

        # add templates only if prefix is not empty
        if request.devicetype in conf.DEVICE_TYPES and conf.TEMPLATE_PREFIX[request.devicetype]:
            if isinstance(orig_template_name, (list, tuple)):
                orig_template_name = list(orig_template_name)

            for t in orig_template_name:
                base_name = t.split('/')[-1]
                new_template_name.append(t.replace(base_name, '%s%s' % (conf.TEMPLATE_PREFIX[request.devicetype], base_name)))

            new_template_name.extend(orig_template_name)
            response.template_name = new_template_name

        response.set_cookie('devicetype', request.devicetype, domain=settings.SESSION_COOKIE_DOMAIN,
                            max_age=conf.DEVICE_TYPE_COOKIE_MAXAGE, expires=self._get_expires())

        return response

    def _get_expires(self):

        expires_time = time.time() + conf.DEVICE_TYPE_COOKIE_MAXAGE
        return cookie_date(expires_time)
