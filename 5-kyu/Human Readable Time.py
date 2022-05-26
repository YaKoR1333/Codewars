def make_readable(seconds):
    ss = str(seconds % 60)
    if len(ss) == 1:
        ss = '0'+ss
    mm = str(seconds // 60 % 60)
    if len(mm) == 1:
        mm = '0'+mm
    hh = str(seconds // 3600 % 100)
    if len(hh) == 1:
        hh = '0'+hh
    return '{}:{}:{}'.format(hh, mm, ss)
