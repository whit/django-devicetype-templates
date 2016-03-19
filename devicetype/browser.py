from . import conf


def check_browser(ua_string):
    """Return device "type" (tablet, mobile, desktop) based on UA string"""

    ua_string = ua_string.lower()

    for t in conf.TABLET_PATTERNS:
        if t in ua_string:
            return conf.DEVICETYPE_TABLET

    for m in conf.MOBILE_PATTERNS:
        if m in ua_string:
            return conf.DEVICETYPE_MOBILE

    return conf.DEVICETYPE_DESKTOP
