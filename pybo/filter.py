#def format_datetime(value, fmt='%Y년 %m월 %d일 %p %I:%M'):
def format_datetime(value, fmt='%Y.%m.%d %I:%M'):
    return value.strftime(fmt)