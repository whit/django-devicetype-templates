from devicetype.conf import MOBILE_PATTERNS, TABLET_PATTERNS


def check_browser(ua_string):
    """Return device "type" (tablet, mobile, desktop) based on UA string"""

    ua_string = ua_string.lower()

    for t in TABLET_PATTERNS:
        if ua_string.find(t) > 0:
            return 'tablet'

    for m in MOBILE_PATTERNS:
        if ua_string.find(m) > 0:
            return 'mobile'

    return 'desktop'
