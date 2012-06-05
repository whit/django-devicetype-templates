def responsive_mode(request):
    return {
        'responsive_mode': getattr(request, 'responsive_mode', 'b'),
        'is_mobile': getattr(request, 'is_mobile', False)
    }
