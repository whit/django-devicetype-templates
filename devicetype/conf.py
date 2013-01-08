from django.conf import settings

MOBILE_PATTERNS = getattr(settings, 'DEVICETYPE_MOBILE_PATTERNS', ('iphone', 'ipod', 'android', 'mobile', 'blackberry',
                                                                   'windows ce', 'opera mini', 'opera mobile', 'palm',
                                                                   'ipad',)
)
TABLET_PATTERNS = getattr(settings, 'DEVICETYPE_TABLET_PATTERNS', ('ipad', 'android 3', 'tablet', 'nexus 7'))

TEMPLATE_PREFIX = getattr(settings, 'DEVICETYPE_TEMPLATE_PREFIX', {
    'desktop': '',
    'mobile': 'mobile/',
    'tablet': 'tablet/',
})

PREFIX_BASENAME = getattr(settings, 'DEVICETYPE_PREFIX_BASENAME', False)

DEVICE_TYPES = ('desktop', 'mobile', 'tablet')
DEFAULT_TYPE = 'desktop'

DEVICETYPE_COOKIE_MAXAGE = 60 * 60 * 4