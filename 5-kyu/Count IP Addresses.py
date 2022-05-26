def ips_between(start, end):
    start_split = start.split('.')
    end_split = end.split('.')
    sum_range = []
    sum_ip_addresses = 0
    sum_range += reversed(tuple(map(lambda x: int(x[0]) - int(x[1]), zip(end_split, start_split))))
    for counter, i in enumerate(sum_range, start=0):
        sum_ip_addresses += i * (256**counter)
    return sum_ip_addresses
