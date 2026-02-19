import calendar

def get_day(d,m, y):
    fdate = calendar.weekday(y, m, d)
    return calendar.day_name[fdate].upper()
