from datetime import datetime

def time_delta(t1, t2):
    fmt = "%a %d %b %Y %H:%M:%S %z"
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    diff = dt1 - dt2
    seconds = diff.total_seconds()
    abs_sec = abs(int(seconds))
    return str(abs_sec)