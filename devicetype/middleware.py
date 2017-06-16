import logging
import time

from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.http import cookie_date

try:
    from django.utils.deprecation import MiddlewareMixin
    Parent = MiddlewareMixin
except ImportError:
    Parent = object

from . import conf
from .browser import check_browser

log = logging.getLogger(__name__)


class DeviceTypeMiddleware(Parent):
    _templates_dict = {}

    def process_request(self, request):

        if conf.DEBUG_DEVICETYPE_NOCOOKIE:
            log.warning('DEBUG_DEVICETYPE_NOCOOKIE is on, '
                        'cookie lifetime is set to %d seconds!' % conf.DEVICETYPE_COOKIE_MAXAGE)

        # force switch device type, set cookie and return redirect
        if 'devicetype' in request.GET and request.GET['devicetype'] in conf.DEVICE_TYPES:
            response = HttpResponseRedirect(request.META['PATH_INFO'])
            response.set_cookie('devicetype', request.GET['devicetype'], domain=settings.SESSION_COOKIE_DOMAIN,
                                max_age=conf.DEVICETYPE_COOKIE_MAXAGE, expires=_get_expires())

            return response

        cookie = request.COOKIES.get('devicetype', None)
        if cookie in conf.DEVICE_TYPES:
            # set type from saved cookie
            request.devicetype = cookie
        elif 'HTTP_USER_AGENT' not in request.META:
            # check type by UA string, if present
            request.devicetype = conf.DEFAULT_TYPE
        else:
            request.devicetype = check_browser(request.META['HTTP_USER_AGENT'])

        request.is_mobile = request.devicetype == conf.DEVICETYPE_MOBILE
        request.is_tablet = request.devicetype == conf.DEVICETYPE_TABLET

        return

    def process_template_response(self, request, response):
        """
        Modify template path(s) to render based on device type and returns response
        """

        key = "%s:%s" % (request.devicetype, response.template_name)
        prefix = conf.TEMPLATE_PREFIX[request.devicetype]

        if key not in self._templates_dict:
            orig_template_name = []
            new_template_name = []

            if isinstance(response.template_name, (list, tuple)):
                orig_template_name.extend(list(response.template_name))
            else:
                orig_template_name.append(response.template_name)

            # add templates only if prefix is not empty
            if request.devicetype in conf.DEVICE_TYPES and prefix:
                if not conf.PREFIX_BASENAME and prefix.endswith('/'):
                    new_template_name = ['%s%s' % (prefix, t) for t in orig_template_name]
                else:
                    for t in orig_template_name:
                        base_name = t.split('/')[-1]
                        new_template_name.append(t.replace(base_name, '%s%s' % (prefix, base_name)))

                new_template_name.extend(orig_template_name)
                self._templates_dict[key] = new_template_name
            else:
                self._templates_dict[key] = orig_template_name

        response.template_name = self._templates_dict[key]

        response.set_cookie('devicetype', request.devicetype, domain=settings.SESSION_COOKIE_DOMAIN,
                            max_age=conf.DEVICETYPE_COOKIE_MAXAGE, expires=_get_expires())

        return response


def _get_expires():

    expires_time = time.time() + conf.DEVICETYPE_COOKIE_MAXAGE
    return cookie_date(expires_time)
