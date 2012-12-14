from django.conf import settings

MOBILE_PATTERNS = getattr(settings, 'DEVICETYPE_MOBILE_PATTERNS', ('iphone', 'ipod', 'android', 'mobile', 'blackberry',
                                                                   'windows ce', 'opera mini', 'opera mobile', 'palm',
                                                                   'ipad',)
)
TABLET_PATTERNS = getattr(settings, 'DEVICETYPE_TABLET_PATTERNS', ('ipad', 'android 3', 'tablet', 'nexus 7'))

"""
Prefixes are variable. When you need prefix template file name, use something like `tablet-`. If you want to have
device-specific templates in subfolders, you can use `tablet/` prefix for example.
"""
TEMPLATE_PREFIX = getattr(settings, 'DEVICETYPE_TEMPLATE_PREFIX', {
    'desktop': '',
    'mobile': 'm-',
    'tablet': 't-',
})

DEVICE_TYPES = ('desktop', 'mobile', 'tablet')

DEVICE_TYPE_COOKIE_MAXAGE = 60 * 60 * 4