def validate_origin_destiny(origin, destiny):
    """Origin and destiny can't be equal!!"""
    return origin != destiny


def validate_start_end_dates(start_date, end_date):
    """Start can't be after end"""
    return start_date > end_date


def validate_start_date(start_date, search_date):
    """Start can't be before search date"""
    return start_date < search_date


def scale_correct(scale):
    """Scale should be in 1..5 or None"""
    valid = False
    if scale is None or int(scale) in [1, 2, 3, 4, 5]:
        valid = True

    return valid
