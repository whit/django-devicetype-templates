def devicetype(request):
    return {
        'devicetype': getattr(request, 'devicetype', 'desktop'),
        'is_mobile': getattr(request, 'is_mobile', False),
        # TODO: detect tablet with big resolution displays
        'big_resolution': False,
    }
