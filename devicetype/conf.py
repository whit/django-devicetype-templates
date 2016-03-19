from django.conf import settings

# for development if you need switch agents oftenly
DEBUG_DEVICETYPE_NOCOOKIE = getattr(settings, 'DEBUG_DEVICETYPE_NOCOOKIE', False)

MOBILE_PATTERNS = getattr(settings, 'DEVICETYPE_MOBILE_PATTERNS', ('iphone', 'ipod', 'android', 'mobile', 'blackberry',
                                                                   'windows ce', 'opera mini', 'opera mobile', 'palm',)
)
TABLET_PATTERNS = getattr(settings, 'DEVICETYPE_TABLET_PATTERNS', ('ipad', 'android 3', 'tablet', 'nexus 7'))

DEVICETYPE_DESKTOP = 'desktop'
DEVICETYPE_TABLET = 'tablet'
DEVICETYPE_MOBILE = 'mobile'

TEMPLATE_PREFIX = getattr(settings, 'DEVICETYPE_TEMPLATE_PREFIX', {
    DEVICETYPE_DESKTOP: '',
    DEVICETYPE_MOBILE: '%s/' % DEVICETYPE_MOBILE,
    DEVICETYPE_TABLET: '%s/' % DEVICETYPE_TABLET,
})

PREFIX_BASENAME = getattr(settings, 'DEVICETYPE_PREFIX_BASENAME', False)

DEVICE_TYPES = (DEVICETYPE_DESKTOP, DEVICETYPE_MOBILE, DEVICETYPE_TABLET)
DEFAULT_TYPE = DEVICETYPE_DESKTOP

if DEBUG_DEVICETYPE_NOCOOKIE:
    DEVICETYPE_COOKIE_MAXAGE = 5
else:
    DEVICETYPE_COOKIE_MAXAGE = 60 * 60 * 6
