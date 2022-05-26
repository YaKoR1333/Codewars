def sum_of_intervals(intervals):
    number = []
    maxn = 0
    minn = 0
    for i in intervals:
        if i[1] > maxn:
            maxn = i[1]
        if i[0] < minn:
            minn = i[0]
    for i in range(0, maxn - minn):
        number.append(0)
    for i in intervals:
        for j in range(i[0]-minn, i[1]-minn):
            number[j] = 1   
    return sum(number)
