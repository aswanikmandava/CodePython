def get_datetime_now(tzinfo="US/Eastern"):
    """
    Returns the current datetime in string format as per the given timezone
    """
    from datetime import datetime
    import pytz
    datetime_format = '%Y-%m-%d %H:%M:%S'
    utc_now = datetime.now(pytz.utc)
    if tzinfo == 'UTC':
        return utc_now.strftime(datetime_format)
    datetime_now = utc_now.astimezone(pytz.timezone(tzinfo))
    datetime_now_str = datetime_now.strftime(datetime_format)
    return datetime_now_str

print(get_datetime_now("UTC"))