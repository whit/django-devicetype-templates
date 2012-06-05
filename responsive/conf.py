from django.conf import settings

MOBILE_PATTERNS = getattr(settings, 'RESPONSIVE_MOBILE_PATTERNS', ('iphone',
    'ipod', 'android', 'mobile', 'blackberry', 'windows ce',
    'opera mini', 'opera mobile', 'palm', 'ipad',)
)
TABLET_PATTERNS = getattr(settings, 'RESPONSIVE_TABLET_PATTERNS', ('ipad',
    'android 3', )
)
