def last_digit(n1, n2):
    if n2 == 0:
        return 1
    if n2 == -1:
        return 1. / n1
    p = last_digit(n1, n2 // 2)
    p *= p
    if n2 % 2:
        p *= n1
    return p % 10
