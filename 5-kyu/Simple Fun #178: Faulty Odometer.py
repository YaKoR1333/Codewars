def faulty_odometer(n):
    return n - count_number4(n)


def count_round_range(k):
    return 10**k - 9**k


def count_number4(n):
    if n < 10:
        return 1 if n >= 4 else 0

    s = str(n)
    digits = len(s)
    hi_digit, lo_n = int(s[0]), int(s[1:])
    if hi_digit < 4:
        return hi_digit * count_round_range(digits - 1) + count_number4(lo_n)
    elif hi_digit == 4:
        return hi_digit * count_round_range(digits - 1) + lo_n + 1
    elif hi_digit > 4:
        return (hi_digit - 1) * count_round_range(digits - 1) + 10 ** (digits - 1) + count_number4(lo_n)
